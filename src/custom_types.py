import hashlib

from sqlalchemy import TypeDecorator, type_coerce, String


class PasswordType(TypeDecorator):
    '''Custom type that will hash plain text password into a sha256 hex string.
    Will also do the corresponding comparison when filtering by it.'''
    impl = String(64)

    def process_bind_param(self, value, dialect):
        return hashlib.sha256(value).hexdigest()

    class comparator_factory(String.comparator_factory):
        def __eq__(self, other):
            local_pw = type_coerce(self.expr, String)
            return local_pw == hashlib.sha256(other).hexdigest()

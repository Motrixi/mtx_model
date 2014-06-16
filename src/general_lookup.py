from sqlalchemy import Column
from sqlalchemy import Integer, String

from custom_types import Base


class WorkflowStatus(Base):
    __tablename__ = 'workflow_status'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=45), nullable=False)


class ProcessState(Base):
    __tablename__ = 'process_state'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=45), nullable=False)


class CreativeType(Base):
    __tablename__ = 'creative_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=45), nullable=False)


class SegmentDataType(Base):
    __tablename__ = 'segment_data_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=45), nullable=False)


class BidType(Base):
    __tablename__ = 'bid_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=45), nullable=False)


class BudgetType(Base):
    __tablename__ = 'budget_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=45), nullable=False)


class SiteType(Base):
    __tablename__ = 'site_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=45), nullable=False)


class TargetType(Base):
    __tablename__ = 'target_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=45), nullable=False)
    table = Column(String(length=45), nullable=True)


class SegmentVendor(Base):
    __tablename__ = 'segment_vendor'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=255), nullable=False)

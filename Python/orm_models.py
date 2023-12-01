from sqlalchemy import create_engine, Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, Session

Base = declarative_base()


class Product(Base):
    """
    Specify model class 'Product' and establish relationships with other tables
    """
    __tablename__ = 'product'
    maker = Column(String, primary_key=True)
    model = Column(String, primary_key=True)
    type = Column(String)
    laptops = relationship('Laptop', back_populates='product')
    pcs = relationship('PC', back_populates='product')
    printers = relationship('Printer', back_populates='product')


class Laptop(Base):
    """
    Specify model class 'Laptop' and establish relationships with other tables
    """
    __tablename__ = 'laptop'
    code = Column(Integer, primary_key=True)
    model = Column(String, ForeignKey('product.model'), nullable=False)
    speed = Column(Integer, nullable=False)
    ram = Column(Integer, nullable=False)
    hd = Column(Integer, nullable=False)
    price = Column(Numeric(10, 2))
    screen = Column(Integer, nullable=False)
    product = relationship('Product', back_populates='laptops')


class PC(Base):
    """
    Specify model class 'PC' and establish relationships with other tables
    """
    __tablename__ = 'pc'
    code = Column(Integer, primary_key=True)
    model = Column(String, ForeignKey('product.model'), nullable=False)
    speed = Column(Integer, nullable=False)
    ram = Column(Integer, nullable=False)
    hd = Column(Integer, nullable=False)
    cd = Column(String, nullable=False)
    price = Column(Numeric(10, 2))
    product = relationship('Product', back_populates='pcs')


class Printer(Base):
    """
    Specify model class 'Printer' and establish relationships with other tables
    """
    __tablename__ = 'printer'
    code = Column(Integer, primary_key=True)
    model = Column(String, ForeignKey('product.model'), nullable=False)
    color = Column(String, nullable=False)
    type = Column(String, nullable=False)
    price = Column(Numeric(10, 2))
    product = relationship('Product', back_populates='printers')

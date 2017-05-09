# from numpy import genfromtxt
import pandas as pd
from time import time
from datetime import datetime
from sqlalchemy import Column, Integer, Float, Date, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def Load_Data(file_name):
    # data = genfromtxt(file_name, delimiter=',', skip_header=1,
    #                   converters={0: lambda s: str(s)})
    df = pd.read_csv(
            file_name,
            sep=',',
            header=0,
            index_col=False,
            # parse_dates=[4],
        )
    return df.values.tolist()

Base = declarative_base()


# IncidntNum,Category,Descript,DayOfWeek,Date,Time,PdDistrict,Resolution,Address,X,Y,Location,PdId
class SFPD(Base):
    # Tell SQLAlchemy what the table name is and if there's any table-specific
    # arguments it should know about
    __tablename__ = 'Raw'
    __table_args__ = {'sqlite_autoincrement': True}
    # tell SQLAlchemy the name of column and its attributes:
    id = Column(Integer, primary_key=True, nullable=False)
    IncidntNum = Column(String)
    Category = Column(String)
    Descript = Column(String)
    DayOfWeek = Column(String)
    Date = Column(Date)
    Time = Column(String)
    PdDistrict = Column(String)
    Resolution = Column(String)
    Address = Column(String)
    X = Column(String)
    Y = Column(String)
    Location = Column(String)
    PdId = Column(String)

if __name__ == "__main__":
    t = time()

    # Create the database
    engine = create_engine('sqlite:///SFPD.db')
    Base.metadata.create_all(engine)

    # Create the session
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()

    try:
        # Source: https://data.sfgov.org/Public-Safety/Police-Department-Incidents/tmnf-yvry
        file_name = "Police_Department_Incidents.csv"
        data = Load_Data(file_name)

        for i in data:
            record = SFPD(**{
                'IncidntNum': i[0],
                'Category': i[1],
                'Descript': i[2],
                'DayOfWeek': i[3],
                'Date': datetime.strptime(i[4], '%m/%d/%Y').date(),
                'Time': i[5],
                'PdDistrict': i[6],
                'Resolution': i[7],
                'Address': i[8],
                'X': i[9],
                'Y': i[10],
                'Location': i[11],
                'PdId': i[12],
            })
            s.add(record)  # Add all the records

        s.commit()  # Attempt to commit all the records
    except Exception as ex:
        print(ex)
        s.rollback()  # Rollback the changes on error
    finally:
        s.close()  # Close the connection
    print ("Time elapsed: " + str(time() - t) + " s.")  # 0.091s

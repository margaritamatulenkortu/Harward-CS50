import os
import csv, sys
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


# def main():
#     with open('/Users/margarita/Documents/HarwardCS50/project1/registration/smallbook.csv', newline='') as csvfile:
#         file = csv.reader(csvfile, delimiter=',', quotechar='|')
#         for row in file:
#             print(row)
#             db.execute(
#                 "INSERT INTO 'smallbook' (isbn, title, author, year) VALUES (%s, %s, %s, %s)", row)
#             db.commit()
#
#
# if __name__ == '__main__':
#     main()


def main():
    filename = 'smallbook.csv'
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        isHeader = True
        try:
            for row in reader:
                if not isHeader:
                    print(row)
                    db.execute(
                    "INSERT INTO smallbook (isbn, title, author, year) VALUES ('%s', '%s', '%s', %s)" % (row[0], row[1], row[2], row[3]))
                    db.commit()
                isHeader = False
        except csv.Error as e:
            sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, e))


if __name__ == '__main__':
    main()

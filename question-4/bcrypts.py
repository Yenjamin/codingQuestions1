import argparse
import bcrypt as bc
import sqlite3

parser = argparse.ArgumentParser(description="nothing yet")
parser.add_argument('-i', '--filename', type=str, help='input file path, input "-" or leave blank for standard input')
parser.add_argument('-r', '--rounds',  type=int, default=18, help='rounds of encryption')
parser.add_argument('-d', '--db_file', type=str, default="bcrypt.cache", help='name of cache results is saved into')
args = parser.parse_args()

def fileRead(path):
    try:
        with open(path) as f:
            lines = f.readlines()
        return(lines[0])
    except IndexError :
        print("empty file")
        return(-1)
    except Exception as e:
        print(e)
        return(-1)

def stdRead():
    text = input("Please enter the string:\n")
    return(text)

def bcrypter(string, round):
    try:
        string = string.encode('utf-8')
        salt = bc.gensalt(rounds=round)
        hashed = bc.hashpw(string, salt)
        return(hashed.decode('utf-8'))
    except Exception as e:
        print(e)
        return(-1)

if __name__ == "__main__":
    if args.filename == None or args.filename == "-":
        string = stdRead()
    else:
        string = fileRead(args.filename)
    try:
        conn = sqlite3.connect(args.db_file)
        c = conn.cursor()

        tables = c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='results'").fetchall()
        if tables == []:
            c.execute("CREATE TABLE results (string text, rounds integer, hashed text)")
        results = c.execute(f"SELECT * FROM results WHERE string='{string}' AND rounds={args.rounds}").fetchall()
        if results == []:
            if string != -1:
                hashed = bcrypter(string, args.rounds)
                if hashed != -1:
                    c.execute(f"INSERT INTO results VALUES ('{string}', {args.rounds}, '{hashed}')")
                    print(hashed)
        else:
            print(results[0][2])
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        if conn:
            conn.close()
from app import server,db


if __name__ == "__main__":
    db.create_all()
    server.run(debug=True)

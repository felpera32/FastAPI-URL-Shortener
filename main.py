import uvicorn
from App.Database.Database import init_db
from App.Connection.connection import getConnection



if __name__ == "__main__":
    conn = getConnection()
    try:
        init_db(conn)
    finally:
        conn.close()
    uvicorn.run(
        "App.Server.server:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )



    
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI, WebSocket
from typing import List
import asyncio

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket, username: str):
        await websocket.accept()
        self.active_connections.append((username, websocket))
        await self.broadcast(f"{username} joined the chat!")

    def disconnect(self, websocket: WebSocket):
        for username, conn in self.active_connections:
            if conn == websocket:
                self.active_connections.remove((username, conn))
                await self.broadcast(f"{username} left the chat.")
                break

    async def broadcast(self, message: str):
        for username, conn in self.active_connections:
            try:
                await conn.send_text(message)
            except Exception as e:
                print(f"Error sending message to client: {e}")

manager = ConnectionManager()

@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(websocket, username)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{username}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


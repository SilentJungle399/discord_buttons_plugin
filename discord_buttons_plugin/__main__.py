from discord.ext import commands
from discord import http
import requests
import inspect
from .types import *
from .models import *

class ButtonsClient():
	def __init__(self, bot):
		self.bot = bot
		self._listeners = {}
		self.bot.add_listener(self.soclistener, 'on_socket_response')

	async def soclistener(self, load):
		if load["t"] == "INTERACTION_CREATE":
			data = load["d"]
			await self.emit(data["data"]["custom_id"], data)

	def click(self, func):
		if not inspect.iscoroutinefunction(func):
			raise TypeError("callback must be a coroutine")
		self.add_listener(func.__name__, func)
		def decorator(*args, **kwargs):
			func(*args, **kwargs)
		return decorator

	def add_listener(self, event, func):
		if "id" not in self._listeners:
			self._listeners[event] = [func]
		else:
			self._listeners[event].append(func)

	async def emit(self, event, data):
		comp = await (InteractionContext(self.bot)).from_json(data)
		if event in self._listeners:
			for i in self._listeners[event]:
				await i(comp)

	async def send(self, content=None, *, 
		channel=None, 
		tts=False,
		embed=None,
		nonce=None,
		allowed_mentions=None,
		components=None
	):
		retcomp = []
		for i in components:
			retcomp.append(i.to_dict())

		if embed:
			embed = embed.to_dict()

		r = http.Route('POST', '/channels/{channel_id}/messages', channel_id = channel)
		await self.bot.http.request(route = r, json = {
			"content": content,
			"tts": tts,
			"embed": embed,
			"nonce": nonce,
			"allowed_mentions": allowed_mentions,
			"components": retcomp
		})

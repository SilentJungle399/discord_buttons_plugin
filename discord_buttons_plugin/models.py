from .types import *
import requests

class InteractionContext:
	def __init__(self, bot):
		self.bot = bot
		self.version = None
		self.type = None
		self.id = None
		self.channel = None
		self.guild = None
		self.token = None
		self.message = None
		self.member = None
		self.data = None

	async def from_json(self, data: dict):
		self.version = data["version"]
		self.type = data["type"]
		self.id = data["id"]
		self.token = data["token"]

		self.channel = self.bot.get_channel(int(data["channel_id"]))
		if not self.channel:
			self.channel = await self.bot.fetch_channel(int(data["channel_id"]))

		self.guild = self.bot.get_guild(int(data["guild_id"]))
		if not self.guild:
			self.guild = await self.bot.fetch_guild(int(data["guild_id"]))

		self.member = self.bot.get_user(int(data["member"]["user"]["id"]))
		if not self.member:
			self.member = await self.bot.fetch_user(int(data["member"]["user"]["id"]))

		self.message = await self.channel.fetch_message(int(data["message"]["id"]))
		self.data = await ContextData().from_json(data["data"])

		return self

	async def reply(
		self, 
		content=None, *, 
		channel=None, 
		tts=False,
		embed=None,
		allowed_mentions=None,
		flags=None
	):

		if embed:
			embed = embed.to_dict()

		url = f"https://discord.com/api/v8/interactions/{self.id}/{self.token}/callback"

		json = {
			"type": 4,
			"data": {
				"content": content,
				"tts": tts,
				"embed": embed,
				"allowed_mentions": allowed_mentions,
				"flags": flags
			}
		}

		requests.post(url, json=json)

class ContextData:
	def __init__(self):
		self.type = None
		self.custom_id = None
	
	async def from_json(self, data):
		self.custom_id = data["custom_id"]

		return self

class ActionRow:
	type = ComponentType.ActionRow
	def __init__(self, components: list):
		self.components = components

	def to_dict(self):
		retcomp = []
		for i in self.components: 
			retcomp.append(i.to_dict())

		return {
			"type": self.type,
			"components": retcomp
		}

class Button:
	type = ComponentType.Button
	def __init__(
		self, 
		label: str = None, *,
		style: ButtonType = ButtonType().Primary,
		custom_id: str = None,
		emoji: str = None,
		url: str = None,
		disabled: bool = False
	):
		self.label = label
		self.style = style
		self.custom_id = custom_id
		self.emoji = emoji
		self.url = url
		self.disabled = disabled

	def to_dict(self):
		ret = {}

		ret["type"] = self.type
		ret["label"] = self.label

		if self.style:
			ret["style"] = self.style

		if self.custom_id:
			ret["custom_id"] = self.custom_id

		if self.emoji:
			ret["emoji"] = self.emoji

		if self.url:
			ret["url"] = self.url

		if self.disabled:
			ret["disabled"] = self.disabled

		return ret

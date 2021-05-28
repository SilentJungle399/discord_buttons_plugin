
# Discord Buttons Plugin

Have a look at an [example](https://github.com/SilentJungle399/discord_buttons_plugin/blob/main/examples/main.py) to quickly get started!

## How to create buttons?
To create buttons, you first need to import the modules and create an instance of `ButtonsClient`
```py
from discord.ext import commands
from discord_buttons_plugin import  *

bot = commands.Bot(command_prefix  =  "!")
buttons = ButtonsClient(bot)
```

Then, you can create buttons using
```py
await buttons.send(
	content = "This is an example message!", 
	channel = ctx.channel.id,
	components = [
		ActionRow([
			Button(
				label="Hello", 
				style=ButtonType().Primary, 
				custom_id="button_one"       
			)
		])
	]
)
```
Breaking it down:
```py
# Create an action row, it takes in one arguement, 
# which is the list of buttons that will go inside
# that action row.
# There can be more than one action rows.
ActionRow([
	...
])

# Create a Button component inside the action row
# And here we have our component
ActionRow([
	Button(
		label = "Button label",
		style = ButtonType().Primary,
		custom_id = "my_button"
	)
])

# You can also make a link button
# You must not add a custom_id in link button
ActionRow([
	Button(
		...
	),
	Button(
		label = "Button label",
		style = ButtonType().Link,
		url = "https://github.com/SilentJungle399/discord_buttons_plugin"
	)
])
```

###  What are the different styled buttons available?
![](https://discord.com/assets/7bb017ce52cfd6575e21c058feb3883b.png)

```py
# To use different styles, the "style" attribute must be changed
Button(
	style = ButtonType().Primary
)

## Other styles are:
# ButtonType().Primary
# ButtonType().Success
# ButtonType().Secondary
# ButtonType().Danger
# ButtonType().Link

# For emoji, You must provide a dictionary with these 3 key-values pairs
Button(
	emoji = {
		"id": None,
		"name": "🙃",
		"animated": False
	},
)
```

## How to listen to button clicks?

To listen to button clicks, you can use `@buttons.click` decorator
```py
# The function name here must be the custom_id you set
# while sending the button component
@buttons.click
async def button_one(ctx):
	await ctx.reply("Hello!")
```
###  What is `ctx` in there?
The `ctx` parameter is an instance of `InteractionContext`
#### Attributes:
- `.id` int : The interaction ID.
- `.token` str : The interaction token.
- `.message` [discord.Message](https://discordpy.readthedocs.io/en/latest/api.html#discord.Message) : The message where buttons are present
- `.channel` [discord.TextChannel](https://discordpy.readthedocs.io/en/latest/api.html#discord.TextChannel) : The channel where buttons are present.
- `.guild` [discord.Guild](https://discordpy.readthedocs.io/en/latest/api.html#discord.Guild) : The guild where buttons are present.
- `.member` [discord.User](https://discordpy.readthedocs.io/en/latest/api.html#discord.User) : The user who clicked the button. Remember this is `discord.User` and not `discord.Member`

#### Methods:
- `await .reply(content=None, *, channel=None, tts=False, embed=None, flags=None)`:
Used while replying to the button click.
The parameters are:
	- `content` str : The message you want to reply with
	- `channel` int : The `id` of the channel where this message must be sent
	- `tts` bool :  Whether this should be text-to-speech
	- `embed` [discord.Embed](https://discordpy.readthedocs.io/en/latest/api.html#discord.Embed) : The rich embed for the content.
	- `flags` MessageFlags : This can either be `None` to send normal messages, or `MessageFlags().EPHEMERAL` to send ephemeral messages.

### What is the difference between ephemeral and normal messages?
- Normal

![](https://media.discordapp.net/attachments/542672943872999424/847901070020837396/unknown.png?width=309&height=242)
- Ephemeral

![](https://media.discordapp.net/attachments/542672943872999424/847887835583479839/unknown.png?width=309&height=242)

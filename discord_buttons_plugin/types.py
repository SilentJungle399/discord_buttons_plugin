class ComponentType:
	"""
	ActionRow: A container for other components
	Button: A clickable button
	"""
	ActionRow = 1
	Button = 2

class ButtonType:
	Primary = 1
	Secondary = 2
	Success = 3
	Danger = 4
	Link = 5

class MessageFlags:
    EPHEMERAL = 1 << 6

from discord import Interaction
from discord import app_commands

class Checks:

  def __init__(self):
    self.superusers: set[int] | None = None

  @staticmethod
  def admin():
    async def predicate(itx: Interaction):
      if not itx.user.guild_permissions.administrator:
        return False
      return True
    return app_commands.check(predicate)

  def superuser(self):
    async def predicate(itx: Interaction):
      if itx.user.id not in self.superusers:
        return False
      return True
    return app_commands.check(predicate)

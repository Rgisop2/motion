from tinydb_async import TinyDBAsync
from tinydb import Query, where
from config import DB_FILE

class Database:
    
    def __init__(self, db_file):
        self.db = TinyDBAsync(db_file)
        self.users_col = self.db.table('users')
        self.channels_col = self.db.table('channels')
        self.User = Query()
        self.Channel = Query()

    def new_user(self, id, name):
        return dict(
            id = id,
            name = name,
            session = None,
        )
    
    def new_channel(self, user_id, channel_id, base_username, interval):
        return dict(
            user_id = user_id,
            channel_id = channel_id,
            base_username = base_username,
            interval = interval,
            is_active = True,
            last_changed = None,
        )
    
    async def add_user(self, id, name):
        user = self.new_user(id, name)
        await self.users_col.insert(user)
    
    async def is_user_exist(self, id):
        user = await self.users_col.get(self.User.id == int(id))
        return bool(user)
    
    async def total_users_count(self):
        count = await self.users_col.count()
        return count

    async def get_all_users(self):
        # TinyDB returns a list of dicts, not a cursor.
        return await self.users_col.all()

    async def delete_user(self, user_id):
        await self.users_col.remove(self.User.id == int(user_id))

    async def set_session(self, id, session):
        await self.users_col.update({'session': session}, self.User.id == int(id))

    async def get_session(self, id):
        user = await self.users_col.get(self.User.id == int(id))
        return user.get('session') if user else None

    async def add_channel(self, user_id, channel_id, base_username, interval):
        channel = self.new_channel(user_id, channel_id, base_username, interval)
        await self.channels_col.insert(channel)

    async def get_user_channels(self, user_id):
        return await self.channels_col.search((self.Channel.user_id == int(user_id)) & (self.Channel.is_active == True))

    async def get_all_active_channels(self):
        return await self.channels_col.search(self.Channel.is_active == True)

    async def stop_channel(self, channel_id):
        await self.channels_col.update({'is_active': False}, self.Channel.channel_id == int(channel_id))

    async def resume_channel(self, channel_id):
        await self.channels_col.update({'is_active': True}, self.Channel.channel_id == int(channel_id))

    async def delete_channel(self, channel_id):
        await self.channels_col.remove(self.Channel.channel_id == int(channel_id))

    async def update_last_changed(self, channel_id, timestamp):
        await self.channels_col.update({'last_changed': timestamp}, self.Channel.channel_id == int(channel_id))

    async def get_channel(self, channel_id):
        return await self.channels_col.get(self.Channel.channel_id == int(channel_id))

db = Database(DB_FILE)


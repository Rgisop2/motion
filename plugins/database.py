from tinydb import TinyDB, Query
from config import DB_FILE

db = TinyDB(DB_FILE)
users_col = db.table('users')
channels_col = db.table('channels')
User = Query()
Channel = Query()

def new_user(id, name):
    return dict(id=id, name=name, session=None)

def new_channel(user_id, channel_id, base_username, interval):
    return dict(
        user_id=user_id,
        channel_id=channel_id,
        base_username=base_username,
        interval=interval,
        is_active=True,
        last_changed=None,
    )

def add_user(id, name):
    users_col.insert(new_user(id, name))

def is_user_exist(id):
    return bool(users_col.get(User.id == int(id)))

def total_users_count():
    return len(users_col)

def get_all_users():
    return users_col.all()

def delete_user(user_id):
    users_col.remove(User.id == int(user_id))

def set_session(id, session):
    users_col.update({'session': session}, User.id == int(id))

def get_session(id):
    user = users_col.get(User.id == int(id))
    return user.get('session') if user else None

def add_channel(user_id, channel_id, base_username, interval):
    channels_col.insert(new_channel(user_id, channel_id, base_username, interval))

def get_user_channels(user_id):
    return channels_col.search((Channel.user_id == int(user_id)) & (Channel.is_active == True))

def get_all_active_channels():
    return channels_col.search(Channel.is_active == True)

def stop_channel(channel_id):
    channels_col.update({'is_active': False}, Channel.channel_id == int(channel_id))

def resume_channel(channel_id):
    channels_col.update({'is_active': True}, Channel.channel_id == int(channel_id))

def delete_channel(channel_id):
    channels_col.remove(Channel.channel_id == int(channel_id))

def update_last_changed(channel_id, timestamp):
    channels_col.update({'last_changed': timestamp}, Channel.channel_id == int(channel_id))

def get_channel(channel_id):
    return channels_col.get(Channel.channel_id == int(channel_id))

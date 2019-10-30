from stravalib.client import Client

TOKEN = "9d995bffece7773e37de6d3d2e2bdaaf09080dbe"
client = Client(access_token=TOKEN)

print (dir(client))
club_members = client.get_club_members()
print (club_members)
print (dir(club_members))
# activities = client.get_activities(limit=1000)
# print (activities)
# print(dir(activities))
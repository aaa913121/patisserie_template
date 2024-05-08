# every 00:00 backup the database using strapi export command(from strapi container)
import os
import datetime

# get the current date
date = datetime.datetime.now().strftime("%Y-%m-%d")

# backup the database
os.system("docker exec -it strapi strapi db:backup")
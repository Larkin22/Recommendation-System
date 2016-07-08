# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 08:33:27 2016

@author: Pavilion
"""
import time

from pydelicious import get_popular,get_userposts,get_urlposts
def initializeUserDict(tag='programming',count=1):
 user_dict={}
 # get the top count' popular posts
 for p1 in get_popular(tag=tag)[0:count]:
# find all users who posted this
  print "working on count" , count
  pst=get_urlposts(p1['url'])
  print "pst len",len(pst)
  for p2 in pst:
   user=p2['user']
   user_dict[user]={}
   print "user="+user
 return user_dict


def fillItems(user_dict):
    all_items={}
    # Find links posted by all users
    for user in user_dict:
        for i in range(3):
            try:
                posts=get_userposts(user)
                break
            except:
                print "Failed "+user+" , retrying"
                time.sleep(4)
            
        for post in posts:
    
         url=post['url']
         print url
         user_dict[user][url]=1
         all_items[url]=1
    
    #Fill in missing items with 0
    for ratings in user_dict.values():
        for item in all_items:
            if item not in ratings:
                ratings[item]=0.0
                

                
                
              
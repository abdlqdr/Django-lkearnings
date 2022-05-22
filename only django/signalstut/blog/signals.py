from django.contrib.auth.signals import user_logged_in, user_login_failed, user_logged_out
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_delete, pre_init, pre_save, post_delete, post_init, post_save, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created

@receiver(user_logged_in, sender=User)
def login_success(sender, request, user,  **kwargs):
    print("--------------------------------------------------")
    print("Logged-in Signal... Run Intro..")
    print("Sender: ", sender)
    print("Request: ", request)
    print("User: ", user)
    print("User-Password: ", user.password)
    print(f"kwargs: {kwargs}")
    
# user_logged_in.connect(login_success, sender=User)        

@receiver(user_login_failed)
def login_failed(sender, credentials, request,  **kwargs):
    print("--------------------------------------------------")
    print("Logged-in-Failed Signal...")
    print("Sender: ", sender)
    print("Request: ", request)
    print("Credentials: ", credentials)
    print(f"kwargs: {kwargs}")
    
# user_login_failed.connect(login_failed)    

@receiver(pre_save, sender=User)
def at_start_save(sender, instance, **kwargs):
    print("--------------------------------------------------")
    print("PreSave Signal...")
    print("Sender: ", sender)
    print("Instance: ", instance)
    print(f"kwargs: {kwargs}")
    
# pre_save.connect(at_start_save, sender=User)    

# @receiver(post_save, sender=User)
def at_end_save(sender, instance, created, **kwargs):
    if created:
        print("--------------------------------------------------")
        print("Post Save Signal... New Record")
        print("Sender: ", sender)
        print("Instance: ", instance)
        print("Created: ", created)
        print(f"kwargs: {kwargs}")
    else:
        print("--------------------------------------------------")
        print("Post Save Signal... update record")
        print("Sender: ", sender)
        print("Instance: ", instance)
        print("Created: ", created)
        print(f"kwargs: {kwargs}")
        
    
post_save.connect(at_end_save, sender=User)    

@receiver(pre_delete, sender=User)
def at_start_delete(sender, instance, **kwargs):
    print("--------------------------------------------------")
    print("Pre delete Signal...")
    print("Sender: ", sender)
    print("Instance: ", instance)
    print(f"kwargs: {kwargs}")
    
# pre_delete.connect(at_start_delete, sender=User)    

# @receiver(post_delete, sender=User)
def at_end_delete(sender, instance, **kwargs):
    print("--------------------------------------------------")
    print("Post delete Signal... ")
    print("Sender: ", sender)
    print("Instance: ", instance)
    print(f"kwargs: {kwargs}")
    
post_delete.connect(at_end_delete, sender=User)  
        
@receiver(pre_init, sender=User)
def at_start_Init(sender, *args, **kwargs):
    print("--------------------------------------------------")
    print("Pre Init Signal...")
    print("Sender: ", sender)
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    
# pre_init.connect(at_start_Init, sender=User)    

# @receiver(post_init, sender=User)
def at_end_Init(sender, *args, **kwargs):
    print("--------------------------------------------------")
    print("Post Init Signal... ")
    print("Sender: ", sender)
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    
post_init.connect(at_end_Init, sender=User) 

# @receiver(request_started)
def at_start_request(sender, environ, **kwargs):
    print("--------------------------------------------------")
    print("At Start Request Signal... ")
    print("Sender: ", sender)
    print("Environ: ", environ)
    print(f"kwargs: {kwargs}")
    
request_started.connect(at_start_request) 

@receiver(request_finished)
def at_end_request(sender, **kwargs):
    print("--------------------------------------------------")
    print("At End Request Signal... ")
    print("Sender: ", sender)
    print(f"kwargs: {kwargs}")
    
# request_finished.connect(at_end_request) 

@receiver(got_request_exception)
def at_request_exception(sender, request, **kwargs):
    print("--------------------------------------------------")
    print("At Request Exception Signal... ")
    print("Sender: ", sender)
    print("Request: ", request)
    print(f"kwargs: {kwargs}")
    
# got_request_exception.connect(at_request_exception) 

@receiver(pre_migrate)
def before_installing_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("--------------------------------------------------")
    print("Before Installing App... ")
    print("Sender: ", sender)
    print("app_config: ", app_config)
    print("Verbosity: ", verbosity)
    print("Interactive: ", interactive)
    print("Using: ", using)
    print("Plan: ", plan)
    print("Apps: ", apps)
    print(f"kwargs: {kwargs}")
    
# pre_migrate.connect(before_installing_app) 

# @receiver(post_migrate)
def aat_end_migrate(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print("--------------------------------------------------")
    print("At end migrate... ")
    print("Sender: ", sender)
    print("app_config: ", app_config)
    print("Verbosity: ", verbosity)
    print("Interactive: ", interactive)
    print("Using: ", using)
    print("Plan: ", plan)
    print("Apps: ", apps)
    print(f"kwargs: {kwargs}")
    
post_migrate.connect(aat_end_migrate) 

@receiver(connection_created)
def connected(sender, connection, **kwargs):
    print("--------------------------------------------------")
    print(" Initial Connecton to Databse... ")
    print("Sender: ", sender)
    print("Connection: ", connection)
    print(f"kwargs: {kwargs}")
    
# connection_created.connect(connected) 

 
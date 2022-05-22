from django.dispatch import Signal, receiver

#Creating Signals
notificaion = Signal(providing_args=["request", "user"])

#Receiver Function
@receiver(notificaion)
def show_notification(sender, **kwargs):
    print("sender:", sender)
    print(f"Kwargs: {kwargs}")
    print("notification", notificaion)
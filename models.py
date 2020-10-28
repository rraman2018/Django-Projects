from django.db import models


class Card(models.Model):

    STATUS_CHOICES = (
        ('TD', 'To-Do'),
        ('IP', 'In-Progress'),
        ('DN', 'Done')
    )
    title = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=1000, blank=True)
    status = models.CharField(
        max_length=2,
        choices=STATUS_CHOICES,
        default='TD'
    )
    # user->card is a 1:many relationship -
    # A user can have 1 or more cards. Therefore, user is the foreign key in card
    owner = models.ForeignKey(
        'auth.User',
        related_name='cards',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{}: {} ({}) - {}'.format(
            self.id,
            self.title,
            self.description,
            self.get_status_display()
        )


# A card may have 0 or more tasks.
class Tasks(models.Model):
    task_description = models.CharField(max_length=250, blank=False) # field name description conflicting with card.description
    done = models.BooleanField(default=False)

    # Declare card as foreign key in Task
    card = models.ForeignKey(
        Card,
        related_name='tasks',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{} by {} for {}'.format(
            self.task_description,
            self.done,
            self.card
        )
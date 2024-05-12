from django.db import models
from ceralan_website.core.base_model import BaseModel


class BusStop(BaseModel):
    service = models.ForeignKey('service.Service', on_delete=models.CASCADE, related_name='bus_stops')
    stop_name = models.CharField(max_length=64, blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=False, null=False)
    departure_time = models.DateTimeField(blank=False, null=False)
    return_time = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return f"{self.service.city} - {self.stop_name} - {self.price}"

    class Meta:
        db_table = 'bus_stop'
        verbose_name = 'Bus Stop'
        verbose_name_plural = 'Bus Stops'
        ordering = ['-created_at']

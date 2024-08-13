from django.db import models

class Extrinsic(models.Model):
    hash = models.CharField(max_length=64, unique=True)  # Assuming hash is a fixed-length string
    netuid = models.IntegerField(null = True)  # Assuming it's an integer
    address = models.CharField(max_length=255, null = True)  # Adjust length as needed
    block_number = models.IntegerField(null = True)  # Assuming block number is an integer
    idx = models.IntegerField(null = True)  # Assuming index is an integer
    block_hash = models.CharField(max_length=64, null = True)  # Assuming hash is a fixed-length string
    signature = models.JSONField(null = True)  # Assuming signature is a dictionary (JSON)
    tip = models.IntegerField(null = True)  # Assuming tip is an integer
    nonce = models.IntegerField(null = True)  # Assuming nonce is an integer
    era = models.CharField(max_length=10, null = True)  # Assuming era is a short string
    call_index = models.CharField(max_length=10, null = True)  # Assuming call index is a short string
    call_function = models.CharField(max_length=100, null = True)  # Adjust length as needed
    call_module = models.CharField(max_length=100, null = True)  # Adjust length as needed
    call_args = models.JSONField(null = True)  # Assuming call_args is a list of dictionaries (JSON)
    result = models.CharField(max_length=20, null = True)  # Assuming result is a short string like 'success'
    events = models.JSONField(null = True)  # Assuming events is a list of dictionaries (JSON)

    def __str__(self):
        return f'Extrinsic {self.hash} at block {self.block_number}'
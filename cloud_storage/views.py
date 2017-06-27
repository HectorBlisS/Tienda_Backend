from django.shortcuts import render
from google.cloud import storage
from django.views.generic import View

# Create your views here.


class CloudView(View):

	def get(self, request, bucket_name="tienda-eric", source_blob_name="13091918_10153993795032211_8964025358436815722_n.jpg"):
		"""List all the files in the bucket"""
		storage_client = storage.Client()
		bucket = storage_client.get_bucket(bucket_name)
		blob = bucket.blob(source_blob_name)

		print (bucket)

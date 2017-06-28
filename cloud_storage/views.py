import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from django.shortcuts import render
from google.cloud import storage
from django.views.generic import View
import datetime
from oauth2client.service_account import ServiceAccountCredentials
from django.shortcuts import render, HttpResponse

import base64

# Create your views here.


class CloudView(View):

	def get(self, request, bucket_name="tienda-eric", source_blob_name="13091918_10153993795032211_8964025358436815722_n.jpg"):
		"""List all the files in the bucket"""
		storage_client = storage.Client()
		bucket = storage_client.get_bucket(bucket_name)
		blob = bucket.blob(source_blob_name)

		print (bucket)

class GetSignedUrl(View):

	def get(self, request):
		now = datetime.datetime.now()
		expiration = int((now-datetime.datetime(1970,1,1)).total_seconds())+600
		stringToSign = "GET\n\naplication/pdf\n"+str(expiration)+"\n\n/tienda-eric/BRIEF.pdf"
		#stringToSign = "GET\n\napllication/pdf\n"+str(current_date)+"x-goog-encryption-algorithm:AES256\nx-goog-meta-foo:bar,baz\n/tienda-eric/BRIEF.pdf"

		creds = ServiceAccountCredentials.from_json_keyfile_name(BASE_DIR+"/tienda-eric-e3120f4dca2e.json")
		client_id = creds.service_account_email
		signature = creds.sign_blob(stringToSign)[1]
		encoded = base64.b64encode(signature)
		final = encoded.decode("utf-8").replace("+", "%2B").replace("/", "%2F")
		base_url = "https://storage.googleapis.com/tienda-eric/BRIEF.pdf"
		final_url = base_url + "?GoogleAccessId=" + "clave-tienda-eric@tienda-eric.iam.gserviceaccount.com" + "&Expires="+ str(expiration) + "&Signature=" + final
		print("final papu",final_url)
		return HttpResponse(final_url)


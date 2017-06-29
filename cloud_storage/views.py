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



"""Ejemplo github"""

import base64
import datetime
import md5
import sys
import time

import Crypto.Hash.SHA256 as SHA256
import Crypto.PublicKey.RSA as RSA
import Crypto.Signature.PKCS1_v1_5 as PKCS1_v1_5
import requests

# The Google Cloud Storage API endpoint. You should not need to change this.
GCS_API_ENDPOINT = 'https://storage.googleapis.com'


class CloudStorageURLSigner(object):
  """Contains methods for generating signed URLs for Google Cloud Storage."""

  def __init__(self, key, client_id_email, gcs_api_endpoint, expiration=None,
               session=None):
    """Creates a CloudStorageURLSigner that can be used to access signed URLs.
    Args:
      key: A PyCrypto private key.
      client_id_email: GCS service account email.
      gcs_api_endpoint: Base URL for GCS API.
      expiration: An instance of datetime.datetime containing the time when the
                  signed URL should expire.
      session: A requests.session.Session to use for issuing requests. If not
               supplied, a new session is created.
    """
    self.key = key
    self.client_id_email = client_id_email
    self.gcs_api_endpoint = gcs_api_endpoint

    self.expiration = expiration or (datetime.datetime.now() +
                                     datetime.timedelta(days=1))
    self.expiration = int(time.mktime(self.expiration.timetuple()))

    self.session = session or requests.Session()

  def _Base64Sign(self, plaintext):
    """Signs and returns a base64-encoded SHA256 digest."""
    shahash = SHA256.new(plaintext)
    signer = PKCS1_v1_5.new(self.key)
    signature_bytes = signer.sign(shahash)
    return base64.b64encode(signature_bytes)

  def _MakeSignatureString(self, verb, path, content_md5, content_type):
    """Creates the signature string for signing according to GCS docs."""
    signature_string = ('{verb}\n'
                        '{content_md5}\n'
                        '{content_type}\n'
                        '{expiration}\n'
                        '{resource}')
    return signature_string.format(verb=verb,
                                   content_md5=content_md5,
                                   content_type=content_type,
                                   expiration=self.expiration,
                                   resource=path)

  def _MakeUrl(self, verb, path, content_type='', content_md5=''):
    """Forms and returns the full signed URL to access GCS."""
    base_url = '%s%s' % (self.gcs_api_endpoint, path)
    signature_string = self._MakeSignatureString(verb, path, content_md5,
                                                 content_type)
    signature_signed = self._Base64Sign(signature_string)
    query_params = {'GoogleAccessId': self.client_id_email,
                    'Expires': str(self.expiration),
                    'Signature': signature_signed}
    return base_url, query_params

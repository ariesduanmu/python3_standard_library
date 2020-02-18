import hashlib
import hmac


def make_digest(message, secret):
	hashed = hmac.new(
		secret,
		message,
		hashlib.sha1
		)
	return hashed.hexdigest().encode('utf-8')
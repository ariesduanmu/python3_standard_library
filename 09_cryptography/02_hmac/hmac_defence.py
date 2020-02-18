import io
import pickle
import hmac

from helpers.simple_object import SimpleObject
from helpers.secret_digest import make_digest


RIGHT_SECRET = b'YELLOW SUBMARINE'
WRONG_SECRET = b'OH I DONOT KNOWN'


def send_data(data, secret):
	out_s = io.BytesIO()
	data = SimpleObject(data)
	pickled_data = pickle.dumps(data)
	digest = make_digest(pickled_data, secret)

	header = b"%s %d\n" % (digest, len(pickled_data))
	print(f"[*] WRITING: {header}")
	out_s.write(header)
	out_s.write(pickled_data)
	out_s.flush()

	return out_s

def receive_data(out_s):
	in_s = io.BytesIO(out_s.getvalue())

	while True:
		first_line = in_s.readline()
		if not first_line:
			break
		print(first_line)
		incoming_digest, incoming_length = first_line.split(b" ")
		incoming_length = int(incoming_length.decode("utf-8"))
		print(f"Read: {incoming_digest} {incoming_length}")

		imcoming_pickled_data = in_s.read(incoming_length)

		actual_digest = make_digest(imcoming_pickled_data, RIGHT_SECRET)
		if hmac.compare_digest(actual_digest, incoming_digest):
			obj = pickle.loads(imcoming_pickled_data)
			print(f"[+] OK: {obj}")
		else:
			print(f"[-] WARNING: Data corruption")

if __name__ == "__main__":
	print("Testing message from sender:")
	sender_out_s = send_data('The right message', RIGHT_SECRET)
	receive_data(sender_out_s)
	print()
	print("Testing message from attacker:")
	attacker_out_s = send_data('I am an attacker', WRONG_SECRET)
	receive_data(attacker_out_s)

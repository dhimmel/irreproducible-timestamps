import hashlib

import bitcoin


def carlisle_method(data, compress=False):
    """
    Use the Carlisle method to generate a bitcoin address the hash of data.

    Args:
        data: bytes, data to hash
        compress: bool, whether to compress the public key

    Returns:
        dictionary with address generation information
    """
    # Compute the sha256 hash of the data
    sha256_hash = hashlib.sha256(data)
    private_key = sha256_hash.hexdigest()

    # Generate public key
    public_key = bitcoin.privkey_to_pubkey(private_key)
    if compress:
        public_key = bitcoin.compress(public_key)

    # Generate bitcoin address
    address = bitcoin.pubkey_to_address(public_key)

    return {
        'private_key': private_key,
        'public_key': public_key,
        'compressed': compress,
        'address': address,
        'url ': 'https://blockchain.info/address/{}'.format(address),
    }

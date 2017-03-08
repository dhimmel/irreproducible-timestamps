# Irreproducible Timestamps

This repository is a replication analysis of the following study:

> **How blockchain-timestamped protocols could improve the trustworthiness of medical science**<br>
[[version 2; referees: 3 approved]](https://doi.org/b2pt)<br>
Greg Irving, John Holden<br>
_F1000Research_ (2016) DOI: [10.12688/f1000research.8114.2](https://doi.org/10.12688/f1000research.8114.2)

See [`addresses.ipynb`](addresses.ipynb) for a notebook which unsuccessfully attempts to verify Irving & Holden's timestamp using the [Carlisle method](http://www.bgcarlisle.com/blog/2014/08/25/proof-of-prespecified-endpoints-in-medical-research-with-the-bitcoin-blockchain/ "Proof of prespecified endpoints in medical research with the bitcoin blockchain").

This findings of this analysis are discussed in a companion blog post at http://blog.dhimmel.com/irreproducible-timestamps/.

## Binder

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org:/repo/dhimmel/irreproducible-timestamps)

Click the badge above to launch this repository in Binder.
If the binder fails to launch, check the [system status](http://mybinder.org/status), since mybinder.org experiences downtime often.
If the binder image is outdated, you can rebuild it [here](http://mybinder.org/status/dhimmel/irreproducible-timestamps).

## Environment

Install the [conda](https://conda.io) environment specified in [`environment.yml`](environment.yml) by running:

```sh
conda env create --file environment.yml
```

Activate with `source activate timestamps`.

## License

Content in this repository is released under a [public domain dedication](LICENSE.md) unless otherwise noted. 

The PDF files in [`f1000`](f1000) are [CC BY 4.0](http://creativecommons.org/licenses/by/4.0/) Licensed.
Please attribute Irving & Holden and _F1000Research_ when reusing those files.

# Synthetic Outbreak Dataset

This dataset is fully synthetic and was generated to emulate common
characteristics of public health outbreak reporting data. It is intended
for exploratory data analysis and methodological experimentation only.
No real public health or personal data is included.

The data generation process is documented in `generate_synthetic_data.py`.


## Assumptions About Disease Spread

The synthetic dataset is built on the following simplifying assumptions:

- The outbreak follows a single-wave pattern, with an initial rise in cases,
  a peak, and a gradual decline.
- The population is assumed to be closed, with no migration effects.
- Transmission dynamics are not explicitly modeled; instead, case counts
  reflect an underlying latent outbreak signal.
- Reported cases are treated as a proxy for true infections and are subject
  to reporting noise and delay.
- Symptom reporting is assumed to correlate imperfectly with case counts and
  may fluctuate independently due to behavioral or reporting effects.

These assumptions intentionally abstract away biological and epidemiological
details to focus on data characteristics rather than disease mechanics.


## Scale Limitations

The dataset has several intentional scale limitations:

- The dataset covers a single region and a limited time horizon
  (approximately six months of daily observations).
- Sample size is small relative to real-world public health surveillance data.
- No demographic, geographic, or genomic dimensions are included.
- The dataset is not suitable for real-world forecasting or policy decisions.

These constraints reflect the scope of an exploratory analysis project rather
than an operational public health system.


## Known Artifacts and Data Issues

The synthetic dataset intentionally includes artifacts commonly observed in
real-world public health data, including:

- Missing values in reported case counts and symptom rates, simulating
  reporting gaps and data collection issues.
- Random noise in all signals, reflecting measurement error and uncertainty.
- Non-uniform testing volume, which may not scale proportionally with case
  counts.
- Temporal autocorrelation introduced by construction, which may exaggerate
  apparent trends.

These characteristics require downstream analysis and modeling workflows
to explicitly handle uncertainty, missing data, and temporal dependence.


## Intended Use and Ethics

This dataset is designed solely for educational and methodological purposes.
It does not represent any real disease, population, or outbreak scenario.

Using synthetic data avoids ethical concerns associated with handling
sensitive or personally identifiable health information while allowing
open experimentation and reproducibility.

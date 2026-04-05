# frappe-swiss-coa

A minimal Frappe app that adds Swiss SME Chart of Accounts templates to ERPNext.

## Templates included

| File | Language | Name |
|------|----------|------|
| `CH_SME_COA_EN.json` | English | CH_SME_with number |
| `CH_PME_COA_FR.json` | French | CH_PME_avec numéro |

Both templates follow the Swiss SME accounting standard (KMU Kontenrahmen) and appear automatically in the **Chart of Accounts** dropdown when creating a company with country set to **Switzerland**.

## Installation

### On a new image (recommended)

Add the app to your `Dockerfile`:

```dockerfile
RUN git clone --depth 1 --branch main \
        https://github.com/liechtjc/frappe-swiss-coa \
        apps/swiss_coa \
    && pip install --no-deps -e apps/swiss_coa \
    && echo "swiss_coa" >> sites/apps.txt
```

Then install on the site:

```bash
bench --site <your-site> install-app swiss_coa
```

### On a running instance

```bash
cd /home/frappe/frappe-bench
git clone --depth 1 --branch main https://github.com/liechtjc/frappe-swiss-coa apps/swiss_coa
./env/bin/pip install --no-deps -e apps/swiss_coa
echo "swiss_coa" >> sites/apps.txt
bench --site <your-site> install-app swiss_coa
```

## Compatibility

- ERPNext v15
- Frappe v15

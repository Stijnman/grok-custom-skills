# Energy Comparator Belgium — Flanders

## Purpose
Compare residential electricity and gas contracts in Flanders on a true like-for-like basis using current tariff cards, official supplier pages, regulator/network tariffs, taxes, discounts, and the user's exact consumption profile.

The skill must never rank suppliers on headline kWh price alone. It must calculate the real estimated annual bill and separate recurring costs from one-time discounts.

## Default market
- Country: Belgium
- Region: Flanders
- Default city: Gent
- Default DSO: Fluvius / Imewo
- Default meter: digital meter
- Default electricity tariff: single-rate unless user specifies day/night
- VAT: use current legally applicable VAT from official/current sources

## Default user profile
Use user-provided values when available. If absent, use:
- Electricity consumption: 3,000 kWh/year
- Gas consumption: 4,000 kWh/year
- Average monthly peak: 4.24 kW
- Solar injection: 0 kWh/year
- EV: no
- Heat pump: no

Never silently replace user values with standard regulator profiles.

## Mandatory suppliers/products
Always attempt to include all currently active residential products from the following suppliers when available in Flanders:

1. ENGIE
   - ENGIE Easy Variable — MANDATORY
   - ENGIE Easy Fixed, if offered
   - ENGIE Flow / Basic / Direct / Dynamic or current equivalents
2. Luminus
3. Eneco
4. TotalEnergies
5. Mega
6. EnergyVision
7. HOA Energy
8. Elegant
9. Ecofix
10. Frank Energie
11. Energy Knights
12. Energie.be
13. DATS 24, if residential supply is active
14. Any newly active Flemish supplier that ranks competitively

Do not merge different suppliers into one row.
Do not omit ENGIE Easy Variable even when another ENGIE product is cheaper.

## Freshness rule
Every run must use current data.

For each supplier/product:
1. Prefer official supplier tariff cards or official product pages.
2. Prefer current regulator/network sources for network tariffs, taxes, levies and capacity tariffs.
3. Use reputable comparison sites only to fill gaps or cross-check.
4. Record the tariff-card month/date.
5. Reject stale pricing when a newer tariff card exists.
6. If current data cannot be verified, mark the row as `UNVERIFIED` instead of inventing a value.

## Sources priority
1. Official supplier tariff card PDF/product page
2. Vlaamse Nutsregulator / CREG / Fluvius
3. Independent comparison sites
4. Other secondary sources

Never use an affiliate or comparison-site headline as the sole source when an official tariff card exists.

## Inputs
Accept these parameters:

```yaml
location: Gent
postcode: optional
region: Flanders
dso: Imewo
electricity_kwh: 3000
gas_kwh: 4000
meter: digital
rate_type: single
average_monthly_peak_kw: 4.24
solar_injection_kwh: 0
solar_production_kwh: 0
ev: false
heat_pump: false
contract_preference: any   # any | fixed | variable | dynamic
include_promotions: true
compare_year_2: true
compare_dynamic: true
max_results: 20
```

If the user gives only consumption values, retain all other defaults.

## Data to collect per electricity product
Collect whenever applicable:

- Supplier
- Product name
- Contract type: fixed / variable / dynamic
- Contract duration
- Energy price in c€/kWh
- Day/night prices when applicable
- Indexation formula
- Fixed annual supplier fee
- Green electricity / GSC / WKK contribution
- Balancing/market fee if explicitly charged
- Smart-meter fee if applicable
- Welcome discount
- Consumption-linked discount
- Cashback
- Bundle discount
- Loyalty conditions
- Direct-debit condition
- E-billing condition
- Required contract duration for discount
- Early-exit implications
- Injection tariff in c€/kWh if solar injection > 0
- Source date
- Source URL/reference

## Data to collect per gas product
Collect whenever applicable:

- Supplier
- Product name
- Contract type
- Gas energy price in c€/kWh
- Indexation formula
- Fixed annual supplier fee
- Welcome discount
- Consumption-linked discount
- Cashback
- Conditions
- Source date
- Source URL/reference

## Regulated electricity costs
For the user's DSO, collect the current:

- Capacity tariff €/kW/year
- Minimum billable capacity if applicable
- Consumption-based distribution tariff c€/kWh
- Data-management fee
- Transmission-related charges
- Federal excise
- Flemish levies
- Other mandatory regulated charges

For digital meters:

```text
billable_peak_kw = max(actual_average_monthly_peak_kw, legal_minimum_peak_kw)
capacity_cost = billable_peak_kw × capacity_tariff_eur_per_kw_year
```

If the exact average monthly peak is unknown, calculate scenarios for at least:
- 2.5 kW
- 3.0 kW
- 4.0 kW
- 4.24 kW
- 5.0 kW
- 6.0 kW

Use the user's actual peak whenever supplied.

## Regulated gas costs
For the user's DSO and annual gas consumption, identify the correct consumption band and collect:

- Fixed distribution fee
- Distribution c€/kWh
- Transport c€/kWh
- Data-management fee
- Federal excise
- Other mandatory levies

Use the exact band applicable to the user's gas consumption.

## Calculation engine

### Electricity supplier component
For a simple tariff:

```text
energy_cost_elec = electricity_kwh × electricity_rate_eur_per_kwh
supplier_elec_before_discount = energy_cost_elec + fixed_supplier_fee + supplier_specific_variable_fees
supplier_elec_year1 = supplier_elec_before_discount - eligible_year1_discounts
supplier_elec_year2 = supplier_elec_before_discount - recurring_discounts_only
```

For block tariffs, calculate each consumption block separately.

Example:

```text
block_1_cost = min(consumption, block_1_limit) × block_1_rate
block_2_cost = max(consumption - block_1_limit, 0) × block_2_rate
```

### Gas supplier component

```text
energy_cost_gas = gas_kwh × gas_rate_eur_per_kwh
supplier_gas_before_discount = energy_cost_gas + fixed_supplier_fee + supplier_specific_fees
supplier_gas_year1 = supplier_gas_before_discount - eligible_year1_discounts
supplier_gas_year2 = supplier_gas_before_discount - recurring_discounts_only
```

### Total electricity

```text
electricity_total_year1 =
  supplier_elec_year1
  + regulated_electricity_network_costs
  + electricity_taxes_and_levies

electricity_total_year2 =
  supplier_elec_year2
  + regulated_electricity_network_costs
  + electricity_taxes_and_levies
```

### Total gas

```text
gas_total_year1 =
  supplier_gas_year1
  + regulated_gas_network_costs
  + gas_taxes_and_levies

gas_total_year2 =
  supplier_gas_year2
  + regulated_gas_network_costs
  + gas_taxes_and_levies
```

### Combined totals

```text
combined_year1 = electricity_total_year1 + gas_total_year1
combined_year2 = electricity_total_year2 + gas_total_year2
monthly_year1 = combined_year1 / 12
monthly_year2 = combined_year2 / 12
```

Also calculate:

```text
promotion_value = combined_year2 - combined_year1
supplier_only_cost = supplier_elec_year1 + supplier_gas_year1
```

## Promotion normalization
Promotions must never be hidden inside the kWh rate.

Show separately:
- Base energy cost
- Fixed fee
- One-time welcome discount
- Usage discount
- Cashback
- Conditions
- Net first-year supplier cost
- Expected second-year supplier cost

If a discount requires 12 months of continuous supply, mark:
`12-MONTH RETENTION REQUIRED`.

If a discount is only for new customers, mark:
`NEW CUSTOMER ONLY`.

If eligibility is unclear, exclude it from the conservative total and show a second `best-case promotional total`.

## Dynamic tariffs
For dynamic contracts:
- Do not compare using a single advertised spot price.
- Use a representative weighted annual price if historical hourly consumption is available.
- Otherwise calculate at least three scenarios:
  - Passive household
  - Flexible household
  - Highly optimized household
- Include supplier markup, balancing fee and fixed fee.
- Clearly label dynamic results as scenarios, not guaranteed prices.

## Solar injection
If `solar_injection_kwh > 0`:
- Collect injection remuneration for each supplier.
- Calculate:

```text
injection_revenue = solar_injection_kwh × injection_rate_eur_per_kwh
net_annual_cost = gross_annual_cost - injection_revenue
```

Rank on net annual cost.

## ENGIE Easy Variable special rule
ENGIE Easy Variable is mandatory in every run.

For ENGIE Easy Variable:
1. Fetch the latest official tariff card for Flanders.
2. Capture current electricity rate/formula.
3. Capture current gas rate/formula.
4. Capture fixed annual fees.
5. Capture all promotions separately.
6. Calculate Year 1 and Year 2.
7. Compare directly against:
   - cheapest ENGIE alternative
   - EnergyVision
   - HOA Energy
   - Ecofix
   - Luminus BasicFlex Online
   - Eneco's cheapest comparable variable product
8. Explicitly state whether ENGIE Easy Variable is:
   - cheaper in Year 1
   - cheaper after promotions expire
   - better/worse on fixed fees
   - better/worse at low gas consumption

Never replace ENGIE Easy Variable with ENGIE Basic or Flow.

## Ranking modes
Produce all of these rankings:

### A. Cheapest Year 1
Rank by combined electricity + gas annual bill including confirmed first-year discounts.

### B. Cheapest Year 2
Rank with one-time promotions removed.

### C. Lowest recurring supplier cost
Rank only supplier-controlled recurring costs.

### D. Best fixed contract
Only fixed products.

### E. Best variable contract
Only variable products.

### F. Best dynamic contract
Only dynamic products, scenario-based.

### G. Best low-gas-consumption contract
Give extra weight to low fixed fees when gas_kwh <= 5,000.

### H. Best no-promo contract
Ignore all one-time discounts.

## Low gas consumption rule
When gas consumption <= 5,000 kWh/year, calculate the effective impact of fixed fees:

```text
fixed_fee_equivalent_cents_per_kwh = annual_fixed_fee / gas_kwh × 100
```

Example:

```text
€50 / 4,000 kWh = 1.25 c€/kWh
€100 / 4,000 kWh = 2.50 c€/kWh
```

Call out suppliers whose low headline gas rate is negated by a large fixed fee.

## Validation
Before final ranking:

1. Check that all calculations use the same user profile.
2. Check that all prices have consistent VAT treatment.
3. Check cents/kWh vs €/kWh conversion.
4. Check that one-time discounts are not counted in Year 2.
5. Check that network charges are not double-counted.
6. Check that supplier-independent network charges do not distort supplier ranking.
7. Check tariff-card dates.
8. Verify ENGIE Easy Variable is present.
9. Flag products with unverified promotional conditions.
10. Recalculate totals independently once before output.

## Output format
Start with a compact winner summary.

Then show:

### User profile
- Location / DSO
- Electricity consumption
- Gas consumption
- Meter type
- Average monthly peak

### Top ranking
Use columns:

| Rank | Supplier | Product | Type | Year 1 €/yr | Year 1 €/mo | Year 2 €/yr | Promo value | Confidence |

Confidence:
- HIGH = official current tariff card + official regulated charges
- MEDIUM = official supplier data with one secondary-source assumption
- LOW = secondary-source pricing or unclear promotion

### Detailed breakdown per top 5
For each:
- Electricity energy cost
- Electricity fixed fee
- Electricity promotions
- Gas energy cost
- Gas fixed fee
- Gas promotions
- Regulated electricity costs
- Regulated gas costs
- Taxes/levies
- Total Year 1
- Total Year 2
- Effective monthly cost

### ENGIE Easy Variable section
Always provide a dedicated subsection:

```text
ENGIE Easy Variable
Year 1: €...
Year 2: €...
Electricity base: ... c€/kWh
Gas base: ... c€/kWh
Fixed fees: €...
Promotions: €...
Difference vs winner: €.../year
Difference vs EnergyVision: €.../year
Verdict: ...
```

### Promotion trap section
Show how much each top product rises after first-year discounts expire.

### Peak sensitivity
When peak is estimated, show combined annual total at multiple capacity peaks.

### Final recommendation
Return exactly these three recommendations:
1. `CHEAPEST NOW`
2. `CHEAPEST WITHOUT PROMOS`
3. `BEST PRICE CERTAINTY`

Also state the expected saving versus the most expensive validated product in the comparison.

### Mandatory closing format (always end every run with this)
**Summary**  
One short paragraph: profile used, Year 1 / Year 2 winner, key reason (usually low fixed fees at ≤5 000 kWh gas or promo vs structural price).

**Final Winner**  
- Product name + Supplier  
- Estimated Year 1 total €  
- Estimated Year 2 total €  
- Why it wins on this exact profile

**Switch contract**  
Provide 1–2 concrete, current, non-affiliate-heavy ways to switch:
- Preferred: direct supplier website or official product page of the winner  
- Reliable independent: https://www.test-aankoop.be (or current Test-Aankoop energy comparator) and/or https://callmepower.be  
- Always mention that the user should verify the exact tariff card month and any remaining promo conditions on the day of signing.

Never end without the Summary + Final Winner + Switch links block.

## Behaviour rules
- Use current web data every run.
- Calculate instead of copying comparison-site annual estimates.
- Prefer official tariff cards.
- Never fabricate missing prices.
- Never hide assumptions.
- Never call a promotional price a structural tariff.
- Never rank on brand reputation.
- Never use standard 17,000 kWh gas consumption when the user supplied another value.
- Do not treat regulated network charges as a supplier advantage.
- Do not claim exact annual cost when a variable index is inherently forward-looking; use `estimated annual cost`.
- Use euros to two decimals in calculations.
- Keep intermediate calculations at full precision and round only displayed results.

## Example invocation

```text
Run Energy Comparator Belgium for Gent, Imewo.
Electricity: 3000 kWh/year.
Gas: 4000 kWh/year.
Digital meter.
Average monthly peak: 4.24 kW.
Include all current fixed, variable and dynamic contracts.
Include ENGIE Easy Variable even if it is not top 10.
Compare Year 1 and Year 2.
Show exact calculation and sources.
```

## Success criteria
The skill succeeds only if:
- current tariffs were checked,
- ENGIE Easy Variable was explicitly evaluated,
- all suppliers were normalized to the same consumption profile,
- promotions were separated from recurring rates,
- Year 1 and Year 2 were both calculated,
- Imewo/Fluvius regulated charges were correctly applied,
- the final ranking is based on estimated total annual euros, not headline kWh prices.

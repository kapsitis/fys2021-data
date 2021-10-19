import pandas as pd

# https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/

def main():
    dframe = pd.read_excel("population-register.ods", engine="odf")
    #dframe.groupby('OldMunicipality')['Population'].sum()

    # Find population, age/gender groups - by old municipality.
    summaryDF = dframe.groupby('OldMunicipality').agg({
        'Population': "sum",
        'YoungMales': "sum",
        'YoungFemales': "sum",
        'WorkingMales': "sum",
        'WorkingFemales': "sum",
        'ElderlyMales': "sum",
        'ElderlyFemales': "sum"
    })

    print('*** Summarize by Old Municipality ***')
    print(summaryDF)
    summaryDF['Young'] = summaryDF['YoungMales'] + summaryDF['YoungFemales']
    summaryDF['Working'] = summaryDF['WorkingMales'] + summaryDF['WorkingFemales']
    summaryDF['Elderly'] = summaryDF['ElderlyMales'] + summaryDF['ElderlyFemales']
    summaryDF1 = summaryDF.drop(
        ['Population', 'YoungMales', 'YoungFemales', 'WorkingMales', 'WorkingFemales', 'ElderlyMales', 'ElderlyFemales'],
        axis=1)
    print()
    print('*** Write out age_groups1.csv ***')
    print(summaryDF1)

    summaryDF1.to_csv('../docs/general-web/age_groups1.csv', sep=',', encoding='utf-8')

if __name__ == '__main__':
    main()

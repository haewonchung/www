from csv import DictReader
from django.core.management import BaseCommand

# Import the model
from recommendation.models import Wine, WineProfile

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    help = "Loads data from wine.csv"

    def handle(self, *args, **options):

        # Show this if the data already exist in the database
        # if Wine.objects.exists():
        #     print('Wine data already loaded...exiting.')
        #     print(ALREDY_LOADED_ERROR_MESSAGE)
        #     return

        # Show this before loading the data into the database
        print("Loading Wine data")

        # Code to load the data into database
        for row in DictReader(open('./Wine.csv')):
            wine = Wine(name=row['Name'], type=row['Type'], region=row['Region'], country=row['Country'],
                        rating=float(row['Rating']), primary_flavors=row['Flavor'], comment=row['Comment'], purchase_link=row['Link'])
            wine.save()
            wine_profile = WineProfile(wine_id=wine.id, body=float(row['Body']), tannin=float(row['Tannic']),
                                       sweetness=float(row['Sweet']), acidity=float(row['Acidic']))
            wine_profile.save()


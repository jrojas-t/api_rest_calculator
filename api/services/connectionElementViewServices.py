from base.models import ConnectionElementView
from api.serializers import ConnectionElementViewSerializer

def getAll(request):
    query = """SELECT
                    companyid AS company_id,
                    companyname AS company_name,
                    countryid AS country_id,
                    countryname AS country_name,
                    regionid AS region_id,
                    regionname AS region_name,
                    areaid AS area_id,
                    areaname AS area_name,
                    areashortname AS area_short_name,
                    connectionelementid AS connection_element_id,
                    connectionelementname AS connection_element_name,
                    connectionelementtypeid AS connection_element_type_id,
                    connectionelementtypename AS connection_element_type_name
                FROM connectionelementview
                ORDER BY regionName, areaName, connectionElementName LIMIT 1 """

    result = ConnectionElementView.objects.raw(query)
    serializer = ConnectionElementViewSerializer(result, many=True)
    return serializer
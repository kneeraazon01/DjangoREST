from rest_framework import serializers
from tests.models import cementCompressive, NewProject

# ! DON'T TOUCH THE CODE BELOW FOR NEWPROJECT


class newProjectserializers(serializers.ModelSerializer):
    class Meta:
        model = NewProject
        fields = [
            "pk",
            "author",
            "project_name",
            "lab_name",
            "contractor",
            "consultant",
            "contract_no",
        ]


# ! DON'T TOUCH THE ABOVE CODE FOR NEWPROJECT


class cementCompressiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = cementCompressive
        fields = [
            "pk",
            "test_name",
            "area_of_cube",
            "volume_of_cube",
            "cube_weight_1",
            "cube_weight_2",
            "cube_weight_3",
            "cube_weight_4",
            "cube_weight_5",
            "cube_weight_6",
            "cube_weight_7",
            "cube_weight_8",
            "cube_weight_9",
            "cube_load_1",
            "cube_load_2",
            "cube_load_3",
            "cube_load_4",
            "cube_load_5",
            "cube_load_6",
            "cube_load_7",
            "cube_load_8",
            "cube_load_9",
        ]


class cementResultCompressiveSerializers(serializers.ModelSerializer):
    class Meta:
        model = cementCompressive
        fields = [
            "test_name",
            "pk",
            "strength_1",
            "strength_2",
            "strength_3",
            "strength_4",
            "strength_5",
            "strength_6",
            "strength_7",
            "strength_8",
            "strength_9",
            "avg_strength_1",
            "avg_strength_2",
            "avg_strength_3",
            "density_1",
            "density_2",
            "density_3",
            "density_4",
            "density_5",
            "density_6",
            "density_7",
            "density_8",
            "density_9",
            "avg_density_1",
            "avg_density_2",
            "avg_density_3",
        ]


class reportInfoCementSerializers(serializers.ModelSerializer):
    class Meta:
        model = cementCompressive
        fields = [
            "test_name",
            "pk",
            "strength_1",
            "strength_2",
            "strength_3",
            "strength_4",
            "strength_5",
            "strength_6",
            "strength_7",
            "strength_8",
            "strength_9",
            "avg_strength_1",
            "avg_strength_2",
            "avg_strength_3",
            "density_1",
            "density_2",
            "density_3",
            "density_4",
            "density_5",
            "density_6",
            "density_7",
            "density_8",
            "density_9",
            "avg_density_1",
            "avg_density_2",
            "avg_density_3",
            "cement_w",
            "sand_w",
            "totalMass",
            "water",
            "W_by_c",
            "sampleLocation",
            "cementSource",
            "waterRequired",
            "NormalConsistencyOfCement",
            "mixPorportion",
            "length_c",
            "breadth_c",
            "height_c",
            "date_of_casting",
        ]

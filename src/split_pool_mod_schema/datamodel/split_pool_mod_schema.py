# Auto generated from split_pool_mod_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-05-02T15:13:17
# Schema: split-pool-mod-schema
#
# id: https://w3id.org/turbomam/split-pool-mod-schema
# description: A Schema with processes for splitting, pooling and modifying material entities. Intended to
#              illustrate solutions for NMDC modeling of NEON metadata and metabolomics data
# license: BSD-3

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
BIOPROJECT = CurieNamespace('BIOPROJECT', 'https://www.ncbi.nlm.nih.gov/bioproject/')
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
NEON_SAMP_UUID = CurieNamespace('NEON_SAMP_UUID', 'https://data.neonscience.org/api/v0/samples/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SPLIT_POOL_MOD_SCHEMA = CurieNamespace('split_pool_mod_schema', 'https://w3id.org/turbomam/split-pool-mod-schema/')
DEFAULT_ = SPLIT_POOL_MOD_SCHEMA


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class DatabaseId(URIorCURIE):
    pass


class MaterialEntityId(NamedThingId):
    pass


class ProcessId(NamedThingId):
    pass


class InformationId(NamedThingId):
    pass


class MicDnaExtractionInSoilDnaSampleId(MaterialEntityId):
    pass


class MicDnaExtractionInSubsampleId(MaterialEntityId):
    pass


class SlsMetagenomicsPoolingInCompositeSampleId(MaterialEntityId):
    pass


class SlsSoilCoreCollectionInGeneticArchiveSample1Id(MaterialEntityId):
    pass


class SlsSoilCoreCollectionInGeneticArchiveSample2Id(MaterialEntityId):
    pass


class SlsSoilCoreCollectionInGeneticArchiveSample3Id(MaterialEntityId):
    pass


class SlsSoilCoreCollectionInGeneticArchiveSample4Id(MaterialEntityId):
    pass


class SlsSoilCoreCollectionInGeneticArchiveSample5Id(MaterialEntityId):
    pass


class SlsSoilCoreCollectionInGeneticSampleId(MaterialEntityId):
    pass


class SlsSoilCoreCollectionInSampleId(MaterialEntityId):
    pass


class SlsSoilMoistureInMoistureSampleId(MaterialEntityId):
    pass


class SlsSoilpHInPhSampleId(MaterialEntityId):
    pass


class MmsMetagenomeSequencingInProcessedSeqFileNameId(MaterialEntityId):
    pass


class SubsampleDnaExtractId(ProcessId):
    pass


class SequencingId(ProcessId):
    pass


class DnaSamplePrepSimpleId(ProcessId):
    pass


class DnaSamplePrepCompositeId(ProcessId):
    pass


class PoolingId(ProcessId):
    pass


class GeneticSamplePrepId(ProcessId):
    pass


class MoistureSamplePrepId(ProcessId):
    pass


class PhSamplePrepId(ProcessId):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    An identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass
class Database(YAMLRoot):
    """
    A possibly heterogeneous collections of data
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.Database
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:Database"
    class_name: ClassVar[str] = "Database"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.Database

    id: Union[str, DatabaseId] = None
    name: Optional[str] = None
    information_set: Optional[Union[Dict[Union[str, InformationId], Union[dict, "Information"]], List[Union[dict, "Information"]]]] = empty_dict()
    material_entity_set: Optional[Union[Dict[Union[str, MaterialEntityId], Union[dict, "MaterialEntity"]], List[Union[dict, "MaterialEntity"]]]] = empty_dict()
    named_thing_set: Optional[Union[Dict[Union[str, NamedThingId], Union[dict, NamedThing]], List[Union[dict, NamedThing]]]] = empty_dict()
    process_set: Optional[Union[Dict[Union[str, ProcessId], Union[dict, "Process"]], List[Union[dict, "Process"]]]] = empty_dict()
    mic_dna_extraction_in_soil_dna_sample_set: Optional[Union[Dict[Union[str, MicDnaExtractionInSoilDnaSampleId], Union[dict, "MicDnaExtractionInSoilDnaSample"]], List[Union[dict, "MicDnaExtractionInSoilDnaSample"]]]] = empty_dict()
    mic_dna_extraction_in_subsample_set: Optional[Union[Dict[Union[str, MicDnaExtractionInSubsampleId], Union[dict, "MicDnaExtractionInSubsample"]], List[Union[dict, "MicDnaExtractionInSubsample"]]]] = empty_dict()
    mms_metagenome_sequencing_in_processed_seq_file_name_set: Optional[Union[Dict[Union[str, MmsMetagenomeSequencingInProcessedSeqFileNameId], Union[dict, "MmsMetagenomeSequencingInProcessedSeqFileName"]], List[Union[dict, "MmsMetagenomeSequencingInProcessedSeqFileName"]]]] = empty_dict()
    sls_metagenomics_pooling_in_composite_sample_set: Optional[Union[Dict[Union[str, SlsMetagenomicsPoolingInCompositeSampleId], Union[dict, "SlsMetagenomicsPoolingInCompositeSample"]], List[Union[dict, "SlsMetagenomicsPoolingInCompositeSample"]]]] = empty_dict()
    sls_soil_core_collection_in_genetic_archive_sample1_set: Optional[Union[Dict[Union[str, SlsSoilCoreCollectionInGeneticArchiveSample1Id], Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample1"]], List[Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample1"]]]] = empty_dict()
    sls_soil_core_collection_in_genetic_archive_sample2_set: Optional[Union[Dict[Union[str, SlsSoilCoreCollectionInGeneticArchiveSample2Id], Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample2"]], List[Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample2"]]]] = empty_dict()
    sls_soil_core_collection_in_genetic_archive_sample3_set: Optional[Union[Dict[Union[str, SlsSoilCoreCollectionInGeneticArchiveSample3Id], Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample3"]], List[Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample3"]]]] = empty_dict()
    sls_soil_core_collection_in_genetic_archive_sample4_set: Optional[Union[Dict[Union[str, SlsSoilCoreCollectionInGeneticArchiveSample4Id], Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample4"]], List[Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample4"]]]] = empty_dict()
    sls_soil_core_collection_in_genetic_archive_sample5_set: Optional[Union[Dict[Union[str, SlsSoilCoreCollectionInGeneticArchiveSample5Id], Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample5"]], List[Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample5"]]]] = empty_dict()
    sls_soil_core_collection_in_genetic_sample_set: Optional[Union[Dict[Union[str, SlsSoilCoreCollectionInGeneticSampleId], Union[dict, "SlsSoilCoreCollectionInGeneticSample"]], List[Union[dict, "SlsSoilCoreCollectionInGeneticSample"]]]] = empty_dict()
    sls_soil_core_collection_in_sample_set: Optional[Union[Dict[Union[str, SlsSoilCoreCollectionInSampleId], Union[dict, "SlsSoilCoreCollectionInSample"]], List[Union[dict, "SlsSoilCoreCollectionInSample"]]]] = empty_dict()
    sls_soil_moisture_in_moisture_sample_set: Optional[Union[Dict[Union[str, SlsSoilMoistureInMoistureSampleId], Union[dict, "SlsSoilMoistureInMoistureSample"]], List[Union[dict, "SlsSoilMoistureInMoistureSample"]]]] = empty_dict()
    sls_soil_ph_in_ph_sample_set: Optional[Union[Dict[Union[str, SlsSoilpHInPhSampleId], Union[dict, "SlsSoilpHInPhSample"]], List[Union[dict, "SlsSoilpHInPhSample"]]]] = empty_dict()
    dna_sample_prep_composite_set: Optional[Union[Dict[Union[str, DnaSamplePrepCompositeId], Union[dict, "DnaSamplePrepComposite"]], List[Union[dict, "DnaSamplePrepComposite"]]]] = empty_dict()
    dna_sample_prep_simple_set: Optional[Union[Dict[Union[str, DnaSamplePrepSimpleId], Union[dict, "DnaSamplePrepSimple"]], List[Union[dict, "DnaSamplePrepSimple"]]]] = empty_dict()
    genetic_sample_prep_set: Optional[Union[Dict[Union[str, GeneticSamplePrepId], Union[dict, "GeneticSamplePrep"]], List[Union[dict, "GeneticSamplePrep"]]]] = empty_dict()
    moisture_sample_prep_set: Optional[Union[Dict[Union[str, MoistureSamplePrepId], Union[dict, "MoistureSamplePrep"]], List[Union[dict, "MoistureSamplePrep"]]]] = empty_dict()
    ph_sample_prep_set: Optional[Union[Dict[Union[str, PhSamplePrepId], Union[dict, "PhSamplePrep"]], List[Union[dict, "PhSamplePrep"]]]] = empty_dict()
    pooling_set: Optional[Union[Dict[Union[str, PoolingId], Union[dict, "Pooling"]], List[Union[dict, "Pooling"]]]] = empty_dict()
    sequencing_set: Optional[Union[Dict[Union[str, SequencingId], Union[dict, "Sequencing"]], List[Union[dict, "Sequencing"]]]] = empty_dict()
    subsample_dna_extract_set: Optional[Union[Dict[Union[str, SubsampleDnaExtractId], Union[dict, "SubsampleDnaExtract"]], List[Union[dict, "SubsampleDnaExtract"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatabaseId):
            self.id = DatabaseId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        self._normalize_inlined_as_list(slot_name="information_set", slot_type=Information, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="material_entity_set", slot_type=MaterialEntity, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="named_thing_set", slot_type=NamedThing, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="process_set", slot_type=Process, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="mic_dna_extraction_in_soil_dna_sample_set", slot_type=MicDnaExtractionInSoilDnaSample, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="mic_dna_extraction_in_subsample_set", slot_type=MicDnaExtractionInSubsample, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="mms_metagenome_sequencing_in_processed_seq_file_name_set", slot_type=MmsMetagenomeSequencingInProcessedSeqFileName, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sls_metagenomics_pooling_in_composite_sample_set", slot_type=SlsMetagenomicsPoolingInCompositeSample, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sls_soil_core_collection_in_genetic_archive_sample1_set", slot_type=SlsSoilCoreCollectionInGeneticArchiveSample1, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sls_soil_core_collection_in_genetic_archive_sample2_set", slot_type=SlsSoilCoreCollectionInGeneticArchiveSample2, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sls_soil_core_collection_in_genetic_archive_sample3_set", slot_type=SlsSoilCoreCollectionInGeneticArchiveSample3, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sls_soil_core_collection_in_genetic_archive_sample4_set", slot_type=SlsSoilCoreCollectionInGeneticArchiveSample4, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sls_soil_core_collection_in_genetic_archive_sample5_set", slot_type=SlsSoilCoreCollectionInGeneticArchiveSample5, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sls_soil_core_collection_in_genetic_sample_set", slot_type=SlsSoilCoreCollectionInGeneticSample, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sls_soil_core_collection_in_sample_set", slot_type=SlsSoilCoreCollectionInSample, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sls_soil_moisture_in_moisture_sample_set", slot_type=SlsSoilMoistureInMoistureSample, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sls_soil_ph_in_ph_sample_set", slot_type=SlsSoilpHInPhSample, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="dna_sample_prep_composite_set", slot_type=DnaSamplePrepComposite, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="dna_sample_prep_simple_set", slot_type=DnaSamplePrepSimple, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="genetic_sample_prep_set", slot_type=GeneticSamplePrep, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="moisture_sample_prep_set", slot_type=MoistureSamplePrep, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ph_sample_prep_set", slot_type=PhSamplePrep, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="pooling_set", slot_type=Pooling, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="sequencing_set", slot_type=Sequencing, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="subsample_dna_extract_set", slot_type=SubsampleDnaExtract, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class MaterialEntity(NamedThing):
    """
    An entity that consists of matter. Has an identity that persists over time.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.MaterialEntity
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:MaterialEntity"
    class_name: ClassVar[str] = "MaterialEntity"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.MaterialEntity

    id: Union[str, MaterialEntityId] = None
    neon_sample_class: Optional[str] = None
    neon_sample_tag: Optional[str] = None
    neon_sample_uuid: Optional[str] = None
    has_children: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()
    has_parents: Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MaterialEntityId):
            self.id = MaterialEntityId(self.id)

        if self.neon_sample_class is not None and not isinstance(self.neon_sample_class, str):
            self.neon_sample_class = str(self.neon_sample_class)

        if self.neon_sample_tag is not None and not isinstance(self.neon_sample_tag, str):
            self.neon_sample_tag = str(self.neon_sample_tag)

        if self.neon_sample_uuid is not None and not isinstance(self.neon_sample_uuid, str):
            self.neon_sample_uuid = str(self.neon_sample_uuid)

        if not isinstance(self.has_children, list):
            self.has_children = [self.has_children] if self.has_children is not None else []
        self.has_children = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_children]

        if not isinstance(self.has_parents, list):
            self.has_parents = [self.has_parents] if self.has_parents is not None else []
        self.has_parents = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.has_parents]

        super().__post_init__(**kwargs)


@dataclass
class Process(NamedThing):
    """
    An entity that unfolds over time. Not composed of matter.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.Process
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:Process"
    class_name: ClassVar[str] = "Process"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.Process

    id: Union[str, ProcessId] = None
    has_inputs: Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]] = empty_list()
    has_outputs: Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessId):
            self.id = ProcessId(self.id)

        if not isinstance(self.has_inputs, list):
            self.has_inputs = [self.has_inputs] if self.has_inputs is not None else []
        self.has_inputs = [v if isinstance(v, MaterialEntityId) else MaterialEntityId(v) for v in self.has_inputs]

        if not isinstance(self.has_outputs, list):
            self.has_outputs = [self.has_outputs] if self.has_outputs is not None else []
        self.has_outputs = [v if isinstance(v, MaterialEntityId) else MaterialEntityId(v) for v in self.has_outputs]

        super().__post_init__(**kwargs)


@dataclass
class Information(NamedThing):
    """
    Anything that informs, or reduces uncertainty. Can be about a material entity or a process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.Information
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:Information"
    class_name: ClassVar[str] = "Information"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.Information

    id: Union[str, InformationId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, InformationId):
            self.id = InformationId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MicDnaExtractionInSoilDnaSample(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.MicDnaExtractionInSoilDnaSample
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:MicDnaExtractionInSoilDnaSample"
    class_name: ClassVar[str] = "MicDnaExtractionInSoilDnaSample"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.MicDnaExtractionInSoilDnaSample

    id: Union[str, MicDnaExtractionInSoilDnaSampleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MicDnaExtractionInSoilDnaSampleId):
            self.id = MicDnaExtractionInSoilDnaSampleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MicDnaExtractionInSubsample(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.MicDnaExtractionInSubsample
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:MicDnaExtractionInSubsample"
    class_name: ClassVar[str] = "MicDnaExtractionInSubsample"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.MicDnaExtractionInSubsample

    id: Union[str, MicDnaExtractionInSubsampleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MicDnaExtractionInSubsampleId):
            self.id = MicDnaExtractionInSubsampleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SlsMetagenomicsPoolingInCompositeSample(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsMetagenomicsPoolingInCompositeSample
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:SlsMetagenomicsPoolingInCompositeSample"
    class_name: ClassVar[str] = "SlsMetagenomicsPoolingInCompositeSample"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsMetagenomicsPoolingInCompositeSample

    id: Union[str, SlsMetagenomicsPoolingInCompositeSampleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SlsMetagenomicsPoolingInCompositeSampleId):
            self.id = SlsMetagenomicsPoolingInCompositeSampleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SlsSoilCoreCollectionInGeneticArchiveSample1(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsSoilCoreCollectionInGeneticArchiveSample1
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:SlsSoilCoreCollectionInGeneticArchiveSample1"
    class_name: ClassVar[str] = "SlsSoilCoreCollectionInGeneticArchiveSample1"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsSoilCoreCollectionInGeneticArchiveSample1

    id: Union[str, SlsSoilCoreCollectionInGeneticArchiveSample1Id] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SlsSoilCoreCollectionInGeneticArchiveSample1Id):
            self.id = SlsSoilCoreCollectionInGeneticArchiveSample1Id(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SlsSoilCoreCollectionInGeneticArchiveSample2(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsSoilCoreCollectionInGeneticArchiveSample2
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:SlsSoilCoreCollectionInGeneticArchiveSample2"
    class_name: ClassVar[str] = "SlsSoilCoreCollectionInGeneticArchiveSample2"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsSoilCoreCollectionInGeneticArchiveSample2

    id: Union[str, SlsSoilCoreCollectionInGeneticArchiveSample2Id] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SlsSoilCoreCollectionInGeneticArchiveSample2Id):
            self.id = SlsSoilCoreCollectionInGeneticArchiveSample2Id(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SlsSoilCoreCollectionInGeneticArchiveSample3(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsSoilCoreCollectionInGeneticArchiveSample3
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:SlsSoilCoreCollectionInGeneticArchiveSample3"
    class_name: ClassVar[str] = "SlsSoilCoreCollectionInGeneticArchiveSample3"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsSoilCoreCollectionInGeneticArchiveSample3

    id: Union[str, SlsSoilCoreCollectionInGeneticArchiveSample3Id] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SlsSoilCoreCollectionInGeneticArchiveSample3Id):
            self.id = SlsSoilCoreCollectionInGeneticArchiveSample3Id(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SlsSoilCoreCollectionInGeneticArchiveSample4(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsSoilCoreCollectionInGeneticArchiveSample4
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:SlsSoilCoreCollectionInGeneticArchiveSample4"
    class_name: ClassVar[str] = "SlsSoilCoreCollectionInGeneticArchiveSample4"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsSoilCoreCollectionInGeneticArchiveSample4

    id: Union[str, SlsSoilCoreCollectionInGeneticArchiveSample4Id] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SlsSoilCoreCollectionInGeneticArchiveSample4Id):
            self.id = SlsSoilCoreCollectionInGeneticArchiveSample4Id(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SlsSoilCoreCollectionInGeneticArchiveSample5(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsSoilCoreCollectionInGeneticArchiveSample5
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:SlsSoilCoreCollectionInGeneticArchiveSample5"
    class_name: ClassVar[str] = "SlsSoilCoreCollectionInGeneticArchiveSample5"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsSoilCoreCollectionInGeneticArchiveSample5

    id: Union[str, SlsSoilCoreCollectionInGeneticArchiveSample5Id] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SlsSoilCoreCollectionInGeneticArchiveSample5Id):
            self.id = SlsSoilCoreCollectionInGeneticArchiveSample5Id(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SlsSoilCoreCollectionInGeneticSample(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsSoilCoreCollectionInGeneticSample
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:SlsSoilCoreCollectionInGeneticSample"
    class_name: ClassVar[str] = "SlsSoilCoreCollectionInGeneticSample"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsSoilCoreCollectionInGeneticSample

    id: Union[str, SlsSoilCoreCollectionInGeneticSampleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SlsSoilCoreCollectionInGeneticSampleId):
            self.id = SlsSoilCoreCollectionInGeneticSampleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SlsSoilCoreCollectionInSample(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsSoilCoreCollectionInSample
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:SlsSoilCoreCollectionInSample"
    class_name: ClassVar[str] = "SlsSoilCoreCollectionInSample"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsSoilCoreCollectionInSample

    id: Union[str, SlsSoilCoreCollectionInSampleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SlsSoilCoreCollectionInSampleId):
            self.id = SlsSoilCoreCollectionInSampleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SlsSoilMoistureInMoistureSample(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsSoilMoistureInMoistureSample
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:SlsSoilMoistureInMoistureSample"
    class_name: ClassVar[str] = "SlsSoilMoistureInMoistureSample"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsSoilMoistureInMoistureSample

    id: Union[str, SlsSoilMoistureInMoistureSampleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SlsSoilMoistureInMoistureSampleId):
            self.id = SlsSoilMoistureInMoistureSampleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SlsSoilpHInPhSample(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsSoilpHInPhSample
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:SlsSoilpHInPhSample"
    class_name: ClassVar[str] = "SlsSoilpHInPhSample"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SlsSoilpHInPhSample

    id: Union[str, SlsSoilpHInPhSampleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SlsSoilpHInPhSampleId):
            self.id = SlsSoilpHInPhSampleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MmsMetagenomeSequencingInProcessedSeqFileName(MaterialEntity):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.MmsMetagenomeSequencingInProcessedSeqFileName
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:MmsMetagenomeSequencingInProcessedSeqFileName"
    class_name: ClassVar[str] = "MmsMetagenomeSequencingInProcessedSeqFileName"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.MmsMetagenomeSequencingInProcessedSeqFileName

    id: Union[str, MmsMetagenomeSequencingInProcessedSeqFileNameId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MmsMetagenomeSequencingInProcessedSeqFileNameId):
            self.id = MmsMetagenomeSequencingInProcessedSeqFileNameId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class SubsampleDnaExtract(Process):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SubsampleDnaExtract
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:SubsampleDnaExtract"
    class_name: ClassVar[str] = "SubsampleDnaExtract"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.SubsampleDnaExtract

    id: Union[str, SubsampleDnaExtractId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubsampleDnaExtractId):
            self.id = SubsampleDnaExtractId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Sequencing(Process):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.Sequencing
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:Sequencing"
    class_name: ClassVar[str] = "Sequencing"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.Sequencing

    id: Union[str, SequencingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SequencingId):
            self.id = SequencingId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DnaSamplePrepSimple(Process):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.DnaSamplePrepSimple
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:DnaSamplePrepSimple"
    class_name: ClassVar[str] = "DnaSamplePrepSimple"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.DnaSamplePrepSimple

    id: Union[str, DnaSamplePrepSimpleId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DnaSamplePrepSimpleId):
            self.id = DnaSamplePrepSimpleId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class DnaSamplePrepComposite(Process):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.DnaSamplePrepComposite
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:DnaSamplePrepComposite"
    class_name: ClassVar[str] = "DnaSamplePrepComposite"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.DnaSamplePrepComposite

    id: Union[str, DnaSamplePrepCompositeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DnaSamplePrepCompositeId):
            self.id = DnaSamplePrepCompositeId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Pooling(Process):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.Pooling
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:Pooling"
    class_name: ClassVar[str] = "Pooling"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.Pooling

    id: Union[str, PoolingId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PoolingId):
            self.id = PoolingId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class GeneticSamplePrep(Process):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.GeneticSamplePrep
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:GeneticSamplePrep"
    class_name: ClassVar[str] = "GeneticSamplePrep"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.GeneticSamplePrep

    id: Union[str, GeneticSamplePrepId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GeneticSamplePrepId):
            self.id = GeneticSamplePrepId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class MoistureSamplePrep(Process):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.MoistureSamplePrep
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:MoistureSamplePrep"
    class_name: ClassVar[str] = "MoistureSamplePrep"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.MoistureSamplePrep

    id: Union[str, MoistureSamplePrepId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MoistureSamplePrepId):
            self.id = MoistureSamplePrepId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class PhSamplePrep(Process):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.PhSamplePrep
    class_class_curie: ClassVar[str] = "split_pool_mod_schema:PhSamplePrep"
    class_name: ClassVar[str] = "PhSamplePrep"
    class_model_uri: ClassVar[URIRef] = SPLIT_POOL_MOD_SCHEMA.PhSamplePrep

    id: Union[str, PhSamplePrepId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PhSamplePrepId):
            self.id = PhSamplePrepId(self.id)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.id, domain=None, range=URIRef,
                   pattern=re.compile(r'[a-zA-Z0-9_]+:[a-zA-Z0-9_]+'))

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.description, domain=None, range=Optional[str])

slots.named_thing_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.named_thing_set, name="named_thing_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('named_thing_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.named_thing_set, domain=Database, range=Optional[Union[Dict[Union[str, NamedThingId], Union[dict, NamedThing]], List[Union[dict, NamedThing]]]])

slots.material_entity_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.material_entity_set, name="material_entity_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('material_entity_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.material_entity_set, domain=Database, range=Optional[Union[Dict[Union[str, MaterialEntityId], Union[dict, "MaterialEntity"]], List[Union[dict, "MaterialEntity"]]]])

slots.process_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.process_set, name="process_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('process_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.process_set, domain=Database, range=Optional[Union[Dict[Union[str, ProcessId], Union[dict, "Process"]], List[Union[dict, "Process"]]]])

slots.information_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.information_set, name="information_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('information_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.information_set, domain=Database, range=Optional[Union[Dict[Union[str, InformationId], Union[dict, "Information"]], List[Union[dict, "Information"]]]])

slots.has_inputs = Slot(uri=SPLIT_POOL_MOD_SCHEMA.has_inputs, name="has_inputs", curie=SPLIT_POOL_MOD_SCHEMA.curie('has_inputs'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.has_inputs, domain=Process, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])

slots.has_outputs = Slot(uri=SPLIT_POOL_MOD_SCHEMA.has_outputs, name="has_outputs", curie=SPLIT_POOL_MOD_SCHEMA.curie('has_outputs'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.has_outputs, domain=Process, range=Optional[Union[Union[str, MaterialEntityId], List[Union[str, MaterialEntityId]]]])

slots.has_children = Slot(uri=SPLIT_POOL_MOD_SCHEMA.has_children, name="has_children", curie=SPLIT_POOL_MOD_SCHEMA.curie('has_children'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.has_children, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.has_parents = Slot(uri=SPLIT_POOL_MOD_SCHEMA.has_parents, name="has_parents", curie=SPLIT_POOL_MOD_SCHEMA.curie('has_parents'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.has_parents, domain=NamedThing, range=Optional[Union[Union[str, NamedThingId], List[Union[str, NamedThingId]]]])

slots.neon_sample_class = Slot(uri=SPLIT_POOL_MOD_SCHEMA.neon_sample_class, name="neon_sample_class", curie=SPLIT_POOL_MOD_SCHEMA.curie('neon_sample_class'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.neon_sample_class, domain=None, range=Optional[str])

slots.neon_sample_tag = Slot(uri=SPLIT_POOL_MOD_SCHEMA.neon_sample_tag, name="neon_sample_tag", curie=SPLIT_POOL_MOD_SCHEMA.curie('neon_sample_tag'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.neon_sample_tag, domain=None, range=Optional[str])

slots.neon_sample_uuid = Slot(uri=SPLIT_POOL_MOD_SCHEMA.neon_sample_uuid, name="neon_sample_uuid", curie=SPLIT_POOL_MOD_SCHEMA.curie('neon_sample_uuid'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.neon_sample_uuid, domain=None, range=Optional[str])

slots.mic_dna_extraction_in_soil_dna_sample_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.mic_dna_extraction_in_soil_dna_sample_set, name="mic_dna_extraction_in_soil_dna_sample_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('mic_dna_extraction_in_soil_dna_sample_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.mic_dna_extraction_in_soil_dna_sample_set, domain=Database, range=Optional[Union[Dict[Union[str, MicDnaExtractionInSoilDnaSampleId], Union[dict, "MicDnaExtractionInSoilDnaSample"]], List[Union[dict, "MicDnaExtractionInSoilDnaSample"]]]])

slots.mic_dna_extraction_in_subsample_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.mic_dna_extraction_in_subsample_set, name="mic_dna_extraction_in_subsample_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('mic_dna_extraction_in_subsample_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.mic_dna_extraction_in_subsample_set, domain=Database, range=Optional[Union[Dict[Union[str, MicDnaExtractionInSubsampleId], Union[dict, "MicDnaExtractionInSubsample"]], List[Union[dict, "MicDnaExtractionInSubsample"]]]])

slots.mms_metagenome_sequencing_in_processed_seq_file_name_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.mms_metagenome_sequencing_in_processed_seq_file_name_set, name="mms_metagenome_sequencing_in_processed_seq_file_name_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('mms_metagenome_sequencing_in_processed_seq_file_name_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.mms_metagenome_sequencing_in_processed_seq_file_name_set, domain=Database, range=Optional[Union[Dict[Union[str, MmsMetagenomeSequencingInProcessedSeqFileNameId], Union[dict, "MmsMetagenomeSequencingInProcessedSeqFileName"]], List[Union[dict, "MmsMetagenomeSequencingInProcessedSeqFileName"]]]])

slots.sls_metagenomics_pooling_in_composite_sample_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.sls_metagenomics_pooling_in_composite_sample_set, name="sls_metagenomics_pooling_in_composite_sample_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('sls_metagenomics_pooling_in_composite_sample_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.sls_metagenomics_pooling_in_composite_sample_set, domain=Database, range=Optional[Union[Dict[Union[str, SlsMetagenomicsPoolingInCompositeSampleId], Union[dict, "SlsMetagenomicsPoolingInCompositeSample"]], List[Union[dict, "SlsMetagenomicsPoolingInCompositeSample"]]]])

slots.sls_soil_core_collection_in_genetic_archive_sample1_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.sls_soil_core_collection_in_genetic_archive_sample1_set, name="sls_soil_core_collection_in_genetic_archive_sample1_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('sls_soil_core_collection_in_genetic_archive_sample1_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.sls_soil_core_collection_in_genetic_archive_sample1_set, domain=Database, range=Optional[Union[Dict[Union[str, SlsSoilCoreCollectionInGeneticArchiveSample1Id], Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample1"]], List[Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample1"]]]])

slots.sls_soil_core_collection_in_genetic_archive_sample2_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.sls_soil_core_collection_in_genetic_archive_sample2_set, name="sls_soil_core_collection_in_genetic_archive_sample2_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('sls_soil_core_collection_in_genetic_archive_sample2_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.sls_soil_core_collection_in_genetic_archive_sample2_set, domain=Database, range=Optional[Union[Dict[Union[str, SlsSoilCoreCollectionInGeneticArchiveSample2Id], Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample2"]], List[Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample2"]]]])

slots.sls_soil_core_collection_in_genetic_archive_sample3_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.sls_soil_core_collection_in_genetic_archive_sample3_set, name="sls_soil_core_collection_in_genetic_archive_sample3_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('sls_soil_core_collection_in_genetic_archive_sample3_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.sls_soil_core_collection_in_genetic_archive_sample3_set, domain=Database, range=Optional[Union[Dict[Union[str, SlsSoilCoreCollectionInGeneticArchiveSample3Id], Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample3"]], List[Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample3"]]]])

slots.sls_soil_core_collection_in_genetic_archive_sample4_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.sls_soil_core_collection_in_genetic_archive_sample4_set, name="sls_soil_core_collection_in_genetic_archive_sample4_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('sls_soil_core_collection_in_genetic_archive_sample4_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.sls_soil_core_collection_in_genetic_archive_sample4_set, domain=Database, range=Optional[Union[Dict[Union[str, SlsSoilCoreCollectionInGeneticArchiveSample4Id], Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample4"]], List[Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample4"]]]])

slots.sls_soil_core_collection_in_genetic_archive_sample5_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.sls_soil_core_collection_in_genetic_archive_sample5_set, name="sls_soil_core_collection_in_genetic_archive_sample5_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('sls_soil_core_collection_in_genetic_archive_sample5_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.sls_soil_core_collection_in_genetic_archive_sample5_set, domain=Database, range=Optional[Union[Dict[Union[str, SlsSoilCoreCollectionInGeneticArchiveSample5Id], Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample5"]], List[Union[dict, "SlsSoilCoreCollectionInGeneticArchiveSample5"]]]])

slots.sls_soil_core_collection_in_genetic_sample_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.sls_soil_core_collection_in_genetic_sample_set, name="sls_soil_core_collection_in_genetic_sample_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('sls_soil_core_collection_in_genetic_sample_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.sls_soil_core_collection_in_genetic_sample_set, domain=Database, range=Optional[Union[Dict[Union[str, SlsSoilCoreCollectionInGeneticSampleId], Union[dict, "SlsSoilCoreCollectionInGeneticSample"]], List[Union[dict, "SlsSoilCoreCollectionInGeneticSample"]]]])

slots.sls_soil_core_collection_in_sample_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.sls_soil_core_collection_in_sample_set, name="sls_soil_core_collection_in_sample_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('sls_soil_core_collection_in_sample_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.sls_soil_core_collection_in_sample_set, domain=Database, range=Optional[Union[Dict[Union[str, SlsSoilCoreCollectionInSampleId], Union[dict, "SlsSoilCoreCollectionInSample"]], List[Union[dict, "SlsSoilCoreCollectionInSample"]]]])

slots.sls_soil_moisture_in_moisture_sample_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.sls_soil_moisture_in_moisture_sample_set, name="sls_soil_moisture_in_moisture_sample_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('sls_soil_moisture_in_moisture_sample_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.sls_soil_moisture_in_moisture_sample_set, domain=Database, range=Optional[Union[Dict[Union[str, SlsSoilMoistureInMoistureSampleId], Union[dict, "SlsSoilMoistureInMoistureSample"]], List[Union[dict, "SlsSoilMoistureInMoistureSample"]]]])

slots.sls_soil_ph_in_ph_sample_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.sls_soil_ph_in_ph_sample_set, name="sls_soil_ph_in_ph_sample_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('sls_soil_ph_in_ph_sample_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.sls_soil_ph_in_ph_sample_set, domain=Database, range=Optional[Union[Dict[Union[str, SlsSoilpHInPhSampleId], Union[dict, "SlsSoilpHInPhSample"]], List[Union[dict, "SlsSoilpHInPhSample"]]]])

slots.dna_sample_prep_composite_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.dna_sample_prep_composite_set, name="dna_sample_prep_composite_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('dna_sample_prep_composite_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.dna_sample_prep_composite_set, domain=Database, range=Optional[Union[Dict[Union[str, DnaSamplePrepCompositeId], Union[dict, "DnaSamplePrepComposite"]], List[Union[dict, "DnaSamplePrepComposite"]]]])

slots.dna_sample_prep_simple_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.dna_sample_prep_simple_set, name="dna_sample_prep_simple_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('dna_sample_prep_simple_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.dna_sample_prep_simple_set, domain=Database, range=Optional[Union[Dict[Union[str, DnaSamplePrepSimpleId], Union[dict, "DnaSamplePrepSimple"]], List[Union[dict, "DnaSamplePrepSimple"]]]])

slots.genetic_sample_prep_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.genetic_sample_prep_set, name="genetic_sample_prep_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('genetic_sample_prep_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.genetic_sample_prep_set, domain=Database, range=Optional[Union[Dict[Union[str, GeneticSamplePrepId], Union[dict, "GeneticSamplePrep"]], List[Union[dict, "GeneticSamplePrep"]]]])

slots.moisture_sample_prep_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.moisture_sample_prep_set, name="moisture_sample_prep_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('moisture_sample_prep_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.moisture_sample_prep_set, domain=Database, range=Optional[Union[Dict[Union[str, MoistureSamplePrepId], Union[dict, "MoistureSamplePrep"]], List[Union[dict, "MoistureSamplePrep"]]]])

slots.ph_sample_prep_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.ph_sample_prep_set, name="ph_sample_prep_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('ph_sample_prep_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.ph_sample_prep_set, domain=Database, range=Optional[Union[Dict[Union[str, PhSamplePrepId], Union[dict, "PhSamplePrep"]], List[Union[dict, "PhSamplePrep"]]]])

slots.pooling_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.pooling_set, name="pooling_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('pooling_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.pooling_set, domain=Database, range=Optional[Union[Dict[Union[str, PoolingId], Union[dict, "Pooling"]], List[Union[dict, "Pooling"]]]])

slots.sequencing_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.sequencing_set, name="sequencing_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('sequencing_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.sequencing_set, domain=Database, range=Optional[Union[Dict[Union[str, SequencingId], Union[dict, "Sequencing"]], List[Union[dict, "Sequencing"]]]])

slots.subsample_dna_extract_set = Slot(uri=SPLIT_POOL_MOD_SCHEMA.subsample_dna_extract_set, name="subsample_dna_extract_set", curie=SPLIT_POOL_MOD_SCHEMA.curie('subsample_dna_extract_set'),
                   model_uri=SPLIT_POOL_MOD_SCHEMA.subsample_dna_extract_set, domain=Database, range=Optional[Union[Dict[Union[str, SubsampleDnaExtractId], Union[dict, "SubsampleDnaExtract"]], List[Union[dict, "SubsampleDnaExtract"]]]])
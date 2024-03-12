# bioimage.io model specification
Specification of the fields used in a bioimage.io-compliant RDF to describe AI models with pretrained weights.

These fields are typically stored in a YAML file which we call a model resource description file (model RDF).

Files referenced in fields which are marked with '∈📦 'are included when packaging the resource to a .zip archive.
## `type`<sub> Literal[model]</sub> = model
Specialized resource type 'model'


## `format_version`<sub> Literal[0.5.0]</sub> = 0.5.0
Version of the bioimage.io model description specification used.
When creating a new model always use the latest micro/patch version described here.
The `format_version` is important for any consumer software to understand how to parse the fields.



## `authors`<sub> Sequence[generic.v0_2.Author]</sub>
The authors are the creators of the model RDF and the primary points of contact.
<details><summary>Sequence[generic.v0_2.Author]

</summary>


generic.v0_2.Author:
### `authors.i.name`<sub> str</sub>
Full name


### `authors.i.affiliation`<sub> Optional[str]</sub> = None
Affiliation


### `authors.i.email`<sub> Optional[Email]</sub> = None
Email


### `authors.i.github_user`<sub> Optional[str]</sub> = None
GitHub user name


### `authors.i.orcid`<sub> Optional</sub> = None
An [ORCID iD](https://support.orcid.org/hc/en-us/sections/360001495313-What-is-ORCID
) in hyphenated groups of 4 digits, (and [valid](
https://support.orcid.org/hc/en-us/articles/360006897674-Structure-of-the-ORCID-Identifier
) as per ISO 7064 11,2.)

Optional[str (AfterValidator(validate_orcid_id))]

</details>

## `cite`<sub> Sequence[generic.v0_2.CiteEntry]</sub>
citations
<details><summary>Sequence[generic.v0_2.CiteEntry]

</summary>


generic.v0_2.CiteEntry:
### `cite.i.text`<sub> str</sub>
free text description


### `cite.i.doi`<sub> Optional[str]</sub> = None
A digital object identifier (DOI) is the prefered citation reference.
See https://www.doi.org/ for details. (alternatively specify `url`)


### `cite.i.url`<sub> Optional[str]</sub> = None
URL to cite (preferably specify a `doi` instead)


</details>

## `description`<sub> str</sub>
A string containing a brief description.


## `inputs`<sub> Sequence[InputTensor]</sub>
Describes the input tensors expected by this model.
<details><summary>Sequence[InputTensor]

</summary>


InputTensor:
### `inputs.i.name`<sub> str</sub>
Tensor name. No duplicates are allowed.


### `inputs.i.description`<sub> str</sub> = \<empty string\>
Brief descripiton of the tensor


### `inputs.i.axes`<sub> Sequence</sub>

<details><summary>Sequence[Union[BatchAxis, ChannelAxis, IndexAxis, TimeAxis, SpaceAxis] (discriminator=type)]

</summary>

Sequence[Union[BatchAxis, ChannelAxis, IndexAxis, TimeAxis, SpaceAxis] (discriminator=type)]

BatchAxis:
#### `inputs.i.axes.i.type`<sub> Literal[batch]</sub> = batch



#### `inputs.i.axes.i.name`<sub> str</sub> = batch
a unique name


#### `inputs.i.axes.i.description`<sub> str</sub> = \<empty string\>



#### `inputs.i.axes.i.size`<sub> ParametrizedBatchSize</sub> = min=1 step=1 step_with='BATCH_AXES'
The axis size.
To specify that this axis' size equals another, an axis name can be given.
Specify another tensor's axis as `<tensor name>.<axis name>`.
<details><summary>ParametrizedBatchSize

</summary>


ParametrizedBatchSize:
##### `inputs.i.axes.i.size.min`<sub> Literal[1]</sub> = 1



##### `inputs.i.axes.i.size.step`<sub> Literal[1]</sub> = 1



##### `inputs.i.axes.i.size.step_with`<sub> Literal[BATCH_AXES]</sub> = BATCH_AXES
name of another axis to resize jointly,
i.e. `n=n_other` for `size = min + n*step`, `size_other = min_other + n_other*step_other`.
To step with an axis of another tensor, use `step_with = <tensor name>.<axis name>`.
`step_with="BATCH_AXES"` is a special value to step jointly with all batch dimensions.



</details>

ChannelAxis:
#### `inputs.i.axes.i.type`<sub> Literal[channel]</sub> = channel



#### `inputs.i.axes.i.name`<sub> str</sub> = channel
a unique name


#### `inputs.i.axes.i.description`<sub> str</sub> = \<empty string\>



#### `inputs.i.axes.i.size`<sub> Union</sub> = #channel_names
The axis size.
To specify that this axis' size equals another, an axis name can be given.
Specify another tensor's axis as `<tensor name>.<axis name>`.
Union[int (Gt(gt=0)), Literal[#channel_names]]

#### `inputs.i.axes.i.channel_names`<sub> Sequence</sub>

<details><summary>Sequence[str*]

</summary>

Sequence of str
(MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))

</details>

IndexAxis:
#### `inputs.i.axes.i.type`<sub> Literal[index]</sub> = index



#### `inputs.i.axes.i.name`<sub> str</sub> = index
a unique name


#### `inputs.i.axes.i.description`<sub> str</sub> = \<empty string\>



#### `inputs.i.axes.i.size`<sub> Union</sub>
The axis size.
To specify that this axis' size equals another, an axis name can be given.
Specify another tensor's axis as `<tensor name>.<axis name>`.
<details><summary>Union[int*, ..., str*]

</summary>

Union of
- int (Gt(gt=0))
- ParametrizedSize
- SizeReference
- str
  (MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))
- str (MaxLen(max_length=33))


ParametrizedSize:
##### `inputs.i.axes.i.size.min`<sub> int</sub>



##### `inputs.i.axes.i.size.step`<sub> int</sub>



##### `inputs.i.axes.i.size.step_with`<sub> Union</sub> = None
name of another axis to resize jointly,
i.e. `n=n_other` for `size = min + n*step`, `size_other = min_other + n_other*step_other`.
To step with an axis of another tensor, use `step_with = <tensor name>.<axis name>`.
`step_with="BATCH_AXES"` is a special value to step jointly with all batch dimensions.

<details><summary>Union[str*, str*, Literal[BATCH_AXES], None]

</summary>

Union of
- str
  (MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))
- str (MaxLen(max_length=33))
- Literal[BATCH_AXES]
- None


</details>

SizeReference:
##### `inputs.i.axes.i.size.reference`<sub> Union</sub>

<details><summary>Union[str*, str*]

</summary>

Union of
- str
  (MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))
- str (MaxLen(max_length=33))


</details>

##### `inputs.i.axes.i.size.offset`<sub> int</sub> = 0



</details>

TimeAxis:
#### `inputs.i.axes.i.type`<sub> Literal[time]</sub> = time



#### `inputs.i.axes.i.name`<sub> str</sub> = time
a unique name


#### `inputs.i.axes.i.description`<sub> str</sub> = \<empty string\>



#### `inputs.i.axes.i.size`<sub> Union</sub>
The axis size.
To specify that this axis' size equals another, an axis name can be given.
Specify another tensor's axis as `<tensor name>.<axis name>`.
<details><summary>Union[int*, ..., str*]

</summary>

Union of
- int (Gt(gt=0))
- ParametrizedSize
- SizeReference
- str
  (MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))
- str (MaxLen(max_length=33))


ParametrizedSize:
##### `inputs.i.axes.i.size.min`<sub> int</sub>



##### `inputs.i.axes.i.size.step`<sub> int</sub>



##### `inputs.i.axes.i.size.step_with`<sub> Union</sub> = None
name of another axis to resize jointly,
i.e. `n=n_other` for `size = min + n*step`, `size_other = min_other + n_other*step_other`.
To step with an axis of another tensor, use `step_with = <tensor name>.<axis name>`.
`step_with="BATCH_AXES"` is a special value to step jointly with all batch dimensions.

<details><summary>Union[str*, str*, Literal[BATCH_AXES], None]

</summary>

Union of
- str
  (MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))
- str (MaxLen(max_length=33))
- Literal[BATCH_AXES]
- None


</details>

SizeReference:
##### `inputs.i.axes.i.size.reference`<sub> Union</sub>

<details><summary>Union[str*, str*]

</summary>

Union of
- str
  (MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))
- str (MaxLen(max_length=33))


</details>

##### `inputs.i.axes.i.size.offset`<sub> int</sub> = 0



</details>

#### `inputs.i.axes.i.unit`<sub> Optional</sub> = None

<details><summary>Optional[Literal[attosecond, ..., zettasecond]]

</summary>

Optional[Literal of
- attosecond
- centisecond
- day
- decisecond
- exasecond
- femtosecond
- gigasecond
- hectosecond
- hour
- kilosecond
- megasecond
- microsecond
- millisecond
- minute
- nanosecond
- petasecond
- picosecond
- second
- terasecond
- yoctosecond
- yottasecond
- zeptosecond
- zettasecond
]

</details>

#### `inputs.i.axes.i.scale`<sub> float</sub> = 1.0



SpaceAxis:
#### `inputs.i.axes.i.type`<sub> Literal[space]</sub> = space



#### `inputs.i.axes.i.name`<sub> str</sub> = x
a unique name


#### `inputs.i.axes.i.description`<sub> str</sub> = \<empty string\>



#### `inputs.i.axes.i.size`<sub> Union</sub>
The axis size.
To specify that this axis' size equals another, an axis name can be given.
Specify another tensor's axis as `<tensor name>.<axis name>`.
<details><summary>Union[int*, ..., str*]

</summary>

Union of
- int (Gt(gt=0))
- ParametrizedSize
- SizeReference
- str
  (MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))
- str (MaxLen(max_length=33))


ParametrizedSize:
##### `inputs.i.axes.i.size.min`<sub> int</sub>



##### `inputs.i.axes.i.size.step`<sub> int</sub>



##### `inputs.i.axes.i.size.step_with`<sub> Union</sub> = None
name of another axis to resize jointly,
i.e. `n=n_other` for `size = min + n*step`, `size_other = min_other + n_other*step_other`.
To step with an axis of another tensor, use `step_with = <tensor name>.<axis name>`.
`step_with="BATCH_AXES"` is a special value to step jointly with all batch dimensions.

<details><summary>Union[str*, str*, Literal[BATCH_AXES], None]

</summary>

Union of
- str
  (MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))
- str (MaxLen(max_length=33))
- Literal[BATCH_AXES]
- None


</details>

SizeReference:
##### `inputs.i.axes.i.size.reference`<sub> Union</sub>

<details><summary>Union[str*, str*]

</summary>

Union of
- str
  (MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))
- str (MaxLen(max_length=33))


</details>

##### `inputs.i.axes.i.size.offset`<sub> int</sub> = 0



</details>

#### `inputs.i.axes.i.unit`<sub> Optional</sub> = None

<details><summary>Optional[Literal[angstrom, ..., zettameter]]

</summary>

Optional[Literal of
- angstrom
- attometer
- centimeter
- decimeter
- exameter
- femtometer
- foot
- gigameter
- hectometer
- inch
- kilometer
- megameter
- meter
- micrometer
- mile
- millimeter
- nanometer
- parsec
- petameter
- picometer
- terameter
- yard
- yoctometer
- yottameter
- zeptometer
- zettameter
]

</details>

#### `inputs.i.axes.i.scale`<sub> float</sub> = 1.0



</details>

### `inputs.i.test_tensor`<sub> Union</sub>
An example tensor to use for testing.
Using the model with the test input tensors is expected to yield the test output tensors.
Each test tensor has be a an ndarray in the
[numpy.lib file format](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#module-numpy.lib.format).
The file extension must be '.npy'.
Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]

### `inputs.i.sample_tensor`<sub> Union</sub> = None
A sample tensor to illustrate a possible input/output for the model,
The sample files primarily serve to inform a human user about an example use case
and are typically stored as HDF5, PNG or TIFF images.
Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath, None]

### `inputs.i.values`<sub> Union</sub>
Description of tensor values, optionally per channel.
If specified per channel, `data_type` needs to match across channels for interval and ratio type values.
<details><summary>Union[Union[NominalTensorValue, OrdinalTensorValue, IntervalTensorValue, RatioTensorValue]*, Sequence[Union[NominalTensorValue, OrdinalTensorValue, IntervalTensorValue, RatioTensorValue]*]]

</summary>

Union of
- Union[NominalTensorValue, OrdinalTensorValue, IntervalTensorValue, RatioTensorValue] (discriminator=type)
- Sequence[Union[NominalTensorValue, OrdinalTensorValue, IntervalTensorValue, RatioTensorValue] (discriminator=type)]


NominalTensorValue:
#### `inputs.i.values.description`<sub> str</sub> = \<empty string\>
Brief descripiton of tensor values


#### `inputs.i.values.type`<sub> Literal[nominal]</sub> = nominal



#### `inputs.i.values.values`<sub> Sequence</sub>

Sequence[Union[int, float, str, bool]]

OrdinalTensorValue:
#### `inputs.i.values.description`<sub> str</sub> = \<empty string\>
Brief descripiton of tensor values


#### `inputs.i.values.type`<sub> Literal[ordinal]</sub> = ordinal



#### `inputs.i.values.values`<sub> Sequence</sub>
values in ascending order
Sequence[Union[int, float, str, bool]]

IntervalTensorValue:
#### `inputs.i.values.description`<sub> str</sub> = \<empty string\>
Brief descripiton of tensor values


#### `inputs.i.values.unit`<sub> Optional</sub> = None

<details><summary>Optional[str*]

</summary>

Optional[str
(None; Len(min_length=1, max_length=None); pattern='^(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^[+-]?[1-9]\\d*)?((·(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^[+-]?[1-9]\\d*)?)|(/(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^+?[1-9]\\d*)?))*$; BeforeValidator(<lambda>))]

</details>

#### `inputs.i.values.factor`<sub> float</sub> = 1.0



#### `inputs.i.values.data_type`<sub> Literal</sub>

Literal[float32, float64, uint8, int8, uint16, int16, uint32, int32, uint64, int64]

#### `inputs.i.values.data_range`<sub> Sequence</sub> = (None, None)
Tuple `(minimum, maximum)` specifying the allowed range of the data in this tensor.
`None` correspond to min/max of what can be expressed by `data_type`.
Sequence[Optional[float], Optional[float]]

#### `inputs.i.values.type`<sub> Literal[interval]</sub> = interval



RatioTensorValue:
#### `inputs.i.values.description`<sub> str</sub> = \<empty string\>
Brief descripiton of tensor values


#### `inputs.i.values.unit`<sub> Optional</sub> = None

<details><summary>Optional[str*]

</summary>

Optional[str
(None; Len(min_length=1, max_length=None); pattern='^(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^[+-]?[1-9]\\d*)?((·(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^[+-]?[1-9]\\d*)?)|(/(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^+?[1-9]\\d*)?))*$; BeforeValidator(<lambda>))]

</details>

#### `inputs.i.values.factor`<sub> float</sub> = 1.0



#### `inputs.i.values.data_type`<sub> Literal</sub>

Literal[float32, float64, uint8, int8, uint16, int16, uint32, int32, uint64, int64]

#### `inputs.i.values.data_range`<sub> Sequence</sub> = (None, None)
Tuple `(minimum, maximum)` specifying the allowed range of the data in this tensor.
`None` correspond to min/max of what can be expressed by `data_type`.
Sequence[Optional[float], Optional[float]]

#### `inputs.i.values.type`<sub> Literal[ratio]</sub> = ratio



#### `inputs.i.values.offset`<sub> float</sub> = 0.0



NominalTensorValue:
#### `inputs.i.values.i.description`<sub> str</sub> = \<empty string\>
Brief descripiton of tensor values


#### `inputs.i.values.i.type`<sub> Literal[nominal]</sub> = nominal



#### `inputs.i.values.i.values`<sub> Sequence</sub>

Sequence[Union[int, float, str, bool]]

OrdinalTensorValue:
#### `inputs.i.values.i.description`<sub> str</sub> = \<empty string\>
Brief descripiton of tensor values


#### `inputs.i.values.i.type`<sub> Literal[ordinal]</sub> = ordinal



#### `inputs.i.values.i.values`<sub> Sequence</sub>
values in ascending order
Sequence[Union[int, float, str, bool]]

IntervalTensorValue:
#### `inputs.i.values.i.description`<sub> str</sub> = \<empty string\>
Brief descripiton of tensor values


#### `inputs.i.values.i.unit`<sub> Optional</sub> = None

<details><summary>Optional[str*]

</summary>

Optional[str
(None; Len(min_length=1, max_length=None); pattern='^(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^[+-]?[1-9]\\d*)?((·(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^[+-]?[1-9]\\d*)?)|(/(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^+?[1-9]\\d*)?))*$; BeforeValidator(<lambda>))]

</details>

#### `inputs.i.values.i.factor`<sub> float</sub> = 1.0



#### `inputs.i.values.i.data_type`<sub> Literal</sub>

Literal[float32, float64, uint8, int8, uint16, int16, uint32, int32, uint64, int64]

#### `inputs.i.values.i.data_range`<sub> Sequence</sub> = (None, None)
Tuple `(minimum, maximum)` specifying the allowed range of the data in this tensor.
`None` correspond to min/max of what can be expressed by `data_type`.
Sequence[Optional[float], Optional[float]]

#### `inputs.i.values.i.type`<sub> Literal[interval]</sub> = interval



RatioTensorValue:
#### `inputs.i.values.i.description`<sub> str</sub> = \<empty string\>
Brief descripiton of tensor values


#### `inputs.i.values.i.unit`<sub> Optional</sub> = None

<details><summary>Optional[str*]

</summary>

Optional[str
(None; Len(min_length=1, max_length=None); pattern='^(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^[+-]?[1-9]\\d*)?((·(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^[+-]?[1-9]\\d*)?)|(/(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^+?[1-9]\\d*)?))*$; BeforeValidator(<lambda>))]

</details>

#### `inputs.i.values.i.factor`<sub> float</sub> = 1.0



#### `inputs.i.values.i.data_type`<sub> Literal</sub>

Literal[float32, float64, uint8, int8, uint16, int16, uint32, int32, uint64, int64]

#### `inputs.i.values.i.data_range`<sub> Sequence</sub> = (None, None)
Tuple `(minimum, maximum)` specifying the allowed range of the data in this tensor.
`None` correspond to min/max of what can be expressed by `data_type`.
Sequence[Optional[float], Optional[float]]

#### `inputs.i.values.i.type`<sub> Literal[ratio]</sub> = ratio



#### `inputs.i.values.i.offset`<sub> float</sub> = 0.0



</details>

### `inputs.i.preprocessing`<sub> Sequence</sub> = ()
Description of how this input should be preprocessed.
<details><summary>Sequence[Union[model.v0_4.Binarize, ..., model.v0_4.ScaleRange]*]

</summary>

Sequence of Union of
- model.v0_4.Binarize
- model.v0_4.Clip
- model.v0_4.ScaleLinear
- model.v0_4.Sigmoid
- model.v0_4.ZeroMeanUnitVariance
- model.v0_4.ScaleRange

(discriminator=name)

model.v0_4.Binarize:
#### `inputs.i.preprocessing.i.name`<sub> Literal[binarize]</sub> = binarize



#### `inputs.i.preprocessing.i.kwargs`<sub> model.v0_4.BinarizeKwargs</sub>
key word arguments
<details><summary>model.v0_4.BinarizeKwargs

</summary>


model.v0_4.BinarizeKwargs:
##### `inputs.i.preprocessing.i.kwargs.threshold`<sub> float</sub>
The fixed threshold


</details>

model.v0_4.Clip:
#### `inputs.i.preprocessing.i.name`<sub> Literal[clip]</sub> = clip



#### `inputs.i.preprocessing.i.kwargs`<sub> model.v0_4.ClipKwargs</sub>
key word arguments
<details><summary>model.v0_4.ClipKwargs

</summary>


model.v0_4.ClipKwargs:
##### `inputs.i.preprocessing.i.kwargs.min`<sub> float</sub>
minimum value for clipping


##### `inputs.i.preprocessing.i.kwargs.max`<sub> float</sub>
maximum value for clipping


</details>

model.v0_4.ScaleLinear:
#### `inputs.i.preprocessing.i.name`<sub> Literal[scale_linear]</sub> = scale_linear



#### `inputs.i.preprocessing.i.kwargs`<sub> model.v0_4.ScaleLinearKwargs</sub>
key word arguments
<details><summary>model.v0_4.ScaleLinearKwargs

</summary>


model.v0_4.ScaleLinearKwargs:
##### `inputs.i.preprocessing.i.kwargs.axes`<sub> Optional</sub> = None
The subset of axes to scale jointly.
For example xy to scale the two image axes for 2d data jointly.
Optional[str (RestrictCharacters(alphabet='czyx'); AfterValidator(validate_unique_entries))]

##### `inputs.i.preprocessing.i.kwargs.gain`<sub> Union[float, Sequence[float]]</sub> = 1.0
multiplicative factor


##### `inputs.i.preprocessing.i.kwargs.offset`<sub> Union[float, Sequence[float]]</sub> = 0.0
additive term


</details>

model.v0_4.Sigmoid:
#### `inputs.i.preprocessing.i.name`<sub> Literal[sigmoid]</sub> = sigmoid



#### `inputs.i.preprocessing.i.kwargs`<sub> model.v0_4.ProcessingKwargs</sub> =
key word arguments


model.v0_4.ZeroMeanUnitVariance:
#### `inputs.i.preprocessing.i.name`<sub> Literal[zero_mean_unit_variance]</sub> = zero_mean_unit_variance



#### `inputs.i.preprocessing.i.kwargs`<sub> model.v0_4.ZeroMeanUnitVarianceK</sub>
key word arguments
<details><summary>model.v0_4.ZeroMeanUnitVarianceKwargs

</summary>

model.v0_4.ZeroMeanUnitVarianceKwargs

model.v0_4.ZeroMeanUnitVarianceKwargs:
##### `inputs.i.preprocessing.i.kwargs.mode`<sub> Literal</sub> = fixed
Mode for computing mean and variance.
| mode | description |
| --- | ---- |
| per_dataset | mean and variance are computed for the entire dataset |
| per_sample | mean and variance are computed for each sample individually |

| fixed | fixed values for mean and variance |

Literal[fixed, per_dataset, per_sample]

##### `inputs.i.preprocessing.i.kwargs.axes`<sub> str</sub>
The subset of axes to normalize jointly.
For example `xy` to normalize the two image axes for 2d data jointly.


##### `inputs.i.preprocessing.i.kwargs.mean`<sub> Union</sub> = None
The mean value(s) to use for `mode: fixed`.
For example `[1.1, 2.2, 3.3]` in the case of a 3 channel image with `axes: xy`.
Union[float, Sequence[float] (MinLen(min_length=1)), None]

##### `inputs.i.preprocessing.i.kwargs.std`<sub> Union</sub> = None
The standard deviation values to use for `mode: fixed`. Analogous to mean.
Union[float, Sequence[float] (MinLen(min_length=1)), None]

##### `inputs.i.preprocessing.i.kwargs.eps`<sub> float</sub> = 1e-06
epsilon for numeric stability: `out = (tensor - mean) / (std + eps)`.


</details>

model.v0_4.ScaleRange:
#### `inputs.i.preprocessing.i.name`<sub> Literal[scale_range]</sub> = scale_range



#### `inputs.i.preprocessing.i.kwargs`<sub> model.v0_4.ScaleRangeKwargs</sub>
key word arguments
<details><summary>model.v0_4.ScaleRangeKwargs

</summary>


model.v0_4.ScaleRangeKwargs:
##### `inputs.i.preprocessing.i.kwargs.mode`<sub> Literal[per_dataset, per_sample]</sub>



##### `inputs.i.preprocessing.i.kwargs.axes`<sub> str</sub>
The subset of axes to normalize jointly.
For example xy to normalize the two image axes for 2d data jointly.


##### `inputs.i.preprocessing.i.kwargs.min_percentile`<sub> float</sub> = 0.0
The lower percentile used for normalization.


##### `inputs.i.preprocessing.i.kwargs.max_percentile`<sub> float</sub> = 100.0
The upper percentile used for normalization
Has to be bigger than `min_percentile`.
The range is 1 to 100 instead of 0 to 100 to avoid mistakenly
accepting percentiles specified in the range 0.0 to 1.0.


##### `inputs.i.preprocessing.i.kwargs.eps`<sub> float</sub> = 1e-06
Epsilon for numeric stability.
`out = (tensor - v_lower) / (v_upper - v_lower + eps)`;
with `v_lower,v_upper` values at the respective percentiles.


##### `inputs.i.preprocessing.i.kwargs.reference_tensor`<sub> Optional</sub> = None
Tensor name to compute the percentiles from. Default: The tensor itself.
For any tensor in `inputs` only input tensor references are allowed.
For a tensor in `outputs` only input tensor refereences are allowed if `mode: per_dataset`
<details><summary>Optional[str*]

</summary>

Optional[str
(MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword))]

</details>

</details>

</details>

</details>

## `license`<sub> Literal</sub>
A [SPDX license identifier](https://spdx.org/licenses/).
We do notsupport custom license beyond the SPDX license list, if you need that please
[open a GitHub issue](https://github.com/bioimage-io/spec-bioimage-io/issues/new/choose)
to discuss your intentions with the community.
<details><summary>Literal[0BSD, ..., ZPL-2.1]

</summary>

Literal of
- 0BSD
- AAL
- Abstyles
- AdaCore-doc
- Adobe-2006
- Adobe-Glyph
- ADSL
- AFL-1.1
- AFL-1.2
- AFL-2.0
- AFL-2.1
- AFL-3.0
- Afmparse
- AGPL-1.0-only
- AGPL-1.0-or-later
- AGPL-3.0-only
- AGPL-3.0-or-later
- Aladdin
- AMDPLPA
- AML
- AMPAS
- ANTLR-PD
- ANTLR-PD-fallback
- Apache-1.0
- Apache-1.1
- Apache-2.0
- APAFML
- APL-1.0
- App-s2p
- APSL-1.0
- APSL-1.1
- APSL-1.2
- APSL-2.0
- Arphic-1999
- Artistic-1.0
- Artistic-1.0-cl8
- Artistic-1.0-Perl
- Artistic-2.0
- ASWF-Digital-Assets-1.0
- ASWF-Digital-Assets-1.1
- Baekmuk
- Bahyph
- Barr
- Beerware
- Bitstream-Charter
- Bitstream-Vera
- BitTorrent-1.0
- BitTorrent-1.1
- blessing
- BlueOak-1.0.0
- Boehm-GC
- Borceux
- Brian-Gladman-3-Clause
- BSD-1-Clause
- BSD-2-Clause
- BSD-2-Clause-Patent
- BSD-2-Clause-Views
- BSD-3-Clause
- BSD-3-Clause-Attribution
- BSD-3-Clause-Clear
- BSD-3-Clause-LBNL
- BSD-3-Clause-Modification
- BSD-3-Clause-No-Military-License
- BSD-3-Clause-No-Nuclear-License
- BSD-3-Clause-No-Nuclear-License-2014
- BSD-3-Clause-No-Nuclear-Warranty
- BSD-3-Clause-Open-MPI
- BSD-4-Clause
- BSD-4-Clause-Shortened
- BSD-4-Clause-UC
- BSD-4.3RENO
- BSD-4.3TAHOE
- BSD-Advertising-Acknowledgement
- BSD-Attribution-HPND-disclaimer
- BSD-Protection
- BSD-Source-Code
- BSL-1.0
- BUSL-1.1
- bzip2-1.0.6
- C-UDA-1.0
- CAL-1.0
- CAL-1.0-Combined-Work-Exception
- Caldera
- CATOSL-1.1
- CC-BY-1.0
- CC-BY-2.0
- CC-BY-2.5
- CC-BY-2.5-AU
- CC-BY-3.0
- CC-BY-3.0-AT
- CC-BY-3.0-DE
- CC-BY-3.0-IGO
- CC-BY-3.0-NL
- CC-BY-3.0-US
- CC-BY-4.0
- CC-BY-NC-1.0
- CC-BY-NC-2.0
- CC-BY-NC-2.5
- CC-BY-NC-3.0
- CC-BY-NC-3.0-DE
- CC-BY-NC-4.0
- CC-BY-NC-ND-1.0
- CC-BY-NC-ND-2.0
- CC-BY-NC-ND-2.5
- CC-BY-NC-ND-3.0
- CC-BY-NC-ND-3.0-DE
- CC-BY-NC-ND-3.0-IGO
- CC-BY-NC-ND-4.0
- CC-BY-NC-SA-1.0
- CC-BY-NC-SA-2.0
- CC-BY-NC-SA-2.0-DE
- CC-BY-NC-SA-2.0-FR
- CC-BY-NC-SA-2.0-UK
- CC-BY-NC-SA-2.5
- CC-BY-NC-SA-3.0
- CC-BY-NC-SA-3.0-DE
- CC-BY-NC-SA-3.0-IGO
- CC-BY-NC-SA-4.0
- CC-BY-ND-1.0
- CC-BY-ND-2.0
- CC-BY-ND-2.5
- CC-BY-ND-3.0
- CC-BY-ND-3.0-DE
- CC-BY-ND-4.0
- CC-BY-SA-1.0
- CC-BY-SA-2.0
- CC-BY-SA-2.0-UK
- CC-BY-SA-2.1-JP
- CC-BY-SA-2.5
- CC-BY-SA-3.0
- CC-BY-SA-3.0-AT
- CC-BY-SA-3.0-DE
- CC-BY-SA-3.0-IGO
- CC-BY-SA-4.0
- CC-PDDC
- CC0-1.0
- CDDL-1.0
- CDDL-1.1
- CDL-1.0
- CDLA-Permissive-1.0
- CDLA-Permissive-2.0
- CDLA-Sharing-1.0
- CECILL-1.0
- CECILL-1.1
- CECILL-2.0
- CECILL-2.1
- CECILL-B
- CECILL-C
- CERN-OHL-1.1
- CERN-OHL-1.2
- CERN-OHL-P-2.0
- CERN-OHL-S-2.0
- CERN-OHL-W-2.0
- CFITSIO
- checkmk
- ClArtistic
- Clips
- CMU-Mach
- CNRI-Jython
- CNRI-Python
- CNRI-Python-GPL-Compatible
- COIL-1.0
- Community-Spec-1.0
- Condor-1.1
- copyleft-next-0.3.0
- copyleft-next-0.3.1
- Cornell-Lossless-JPEG
- CPAL-1.0
- CPL-1.0
- CPOL-1.02
- Crossword
- CrystalStacker
- CUA-OPL-1.0
- Cube
- curl
- D-FSL-1.0
- diffmark
- DL-DE-BY-2.0
- DOC
- Dotseqn
- DRL-1.0
- DSDP
- dtoa
- dvipdfm
- ECL-1.0
- ECL-2.0
- EFL-1.0
- EFL-2.0
- eGenix
- Elastic-2.0
- Entessa
- EPICS
- EPL-1.0
- EPL-2.0
- ErlPL-1.1
- etalab-2.0
- EUDatagrid
- EUPL-1.0
- EUPL-1.1
- EUPL-1.2
- Eurosym
- Fair
- FDK-AAC
- Frameworx-1.0
- FreeBSD-DOC
- FreeImage
- FSFAP
- FSFUL
- FSFULLR
- FSFULLRWD
- FTL
- GD
- GFDL-1.1-invariants-only
- GFDL-1.1-invariants-or-later
- GFDL-1.1-no-invariants-only
- GFDL-1.1-no-invariants-or-later
- GFDL-1.1-only
- GFDL-1.1-or-later
- GFDL-1.2-invariants-only
- GFDL-1.2-invariants-or-later
- GFDL-1.2-no-invariants-only
- GFDL-1.2-no-invariants-or-later
- GFDL-1.2-only
- GFDL-1.2-or-later
- GFDL-1.3-invariants-only
- GFDL-1.3-invariants-or-later
- GFDL-1.3-no-invariants-only
- GFDL-1.3-no-invariants-or-later
- GFDL-1.3-only
- GFDL-1.3-or-later
- Giftware
- GL2PS
- Glide
- Glulxe
- GLWTPL
- gnuplot
- GPL-1.0-only
- GPL-1.0-or-later
- GPL-2.0-only
- GPL-2.0-or-later
- GPL-3.0-only
- GPL-3.0-or-later
- Graphics-Gems
- gSOAP-1.3b
- HaskellReport
- Hippocratic-2.1
- HP-1986
- HPND
- HPND-export-US
- HPND-Markus-Kuhn
- HPND-sell-variant
- HPND-sell-variant-MIT-disclaimer
- HTMLTIDY
- IBM-pibs
- ICU
- IEC-Code-Components-EULA
- IJG
- IJG-short
- ImageMagick
- iMatix
- Imlib2
- Info-ZIP
- Inner-Net-2.0
- Intel
- Intel-ACPI
- Interbase-1.0
- IPA
- IPL-1.0
- ISC
- Jam
- JasPer-2.0
- JPL-image
- JPNIC
- JSON
- Kazlib
- Knuth-CTAN
- LAL-1.2
- LAL-1.3
- Latex2e
- Latex2e-translated-notice
- Leptonica
- LGPL-2.0-only
- LGPL-2.0-or-later
- LGPL-2.1-only
- LGPL-2.1-or-later
- LGPL-3.0-only
- LGPL-3.0-or-later
- LGPLLR
- Libpng
- libpng-2.0
- libselinux-1.0
- libtiff
- libutil-David-Nugent
- LiLiQ-P-1.1
- LiLiQ-R-1.1
- LiLiQ-Rplus-1.1
- Linux-man-pages-1-para
- Linux-man-pages-copyleft
- Linux-man-pages-copyleft-2-para
- Linux-man-pages-copyleft-var
- Linux-OpenIB
- LOOP
- LPL-1.0
- LPL-1.02
- LPPL-1.0
- LPPL-1.1
- LPPL-1.2
- LPPL-1.3a
- LPPL-1.3c
- LZMA-SDK-9.11-to-9.20
- LZMA-SDK-9.22
- MakeIndex
- Martin-Birgmeier
- metamail
- Minpack
- MirOS
- MIT
- MIT-0
- MIT-advertising
- MIT-CMU
- MIT-enna
- MIT-feh
- MIT-Festival
- MIT-Modern-Variant
- MIT-open-group
- MIT-Wu
- MITNFA
- Motosoto
- mpi-permissive
- mpich2
- MPL-1.0
- MPL-1.1
- MPL-2.0
- MPL-2.0-no-copyleft-exception
- mplus
- MS-LPL
- MS-PL
- MS-RL
- MTLL
- MulanPSL-1.0
- MulanPSL-2.0
- Multics
- Mup
- NAIST-2003
- NASA-1.3
- Naumen
- NBPL-1.0
- NCGL-UK-2.0
- NCSA
- Net-SNMP
- NetCDF
- Newsletr
- NGPL
- NICTA-1.0
- NIST-PD
- NIST-PD-fallback
- NIST-Software
- NLOD-1.0
- NLOD-2.0
- NLPL
- Nokia
- NOSL
- Noweb
- NPL-1.0
- NPL-1.1
- NPOSL-3.0
- NRL
- NTP
- NTP-0
- O-UDA-1.0
- OCCT-PL
- OCLC-2.0
- ODbL-1.0
- ODC-By-1.0
- OFFIS
- OFL-1.0
- OFL-1.0-no-RFN
- OFL-1.0-RFN
- OFL-1.1
- OFL-1.1-no-RFN
- OFL-1.1-RFN
- OGC-1.0
- OGDL-Taiwan-1.0
- OGL-Canada-2.0
- OGL-UK-1.0
- OGL-UK-2.0
- OGL-UK-3.0
- OGTSL
- OLDAP-1.1
- OLDAP-1.2
- OLDAP-1.3
- OLDAP-1.4
- OLDAP-2.0
- OLDAP-2.0.1
- OLDAP-2.1
- OLDAP-2.2
- OLDAP-2.2.1
- OLDAP-2.2.2
- OLDAP-2.3
- OLDAP-2.4
- OLDAP-2.5
- OLDAP-2.6
- OLDAP-2.7
- OLDAP-2.8
- OLFL-1.3
- OML
- OpenPBS-2.3
- OpenSSL
- OPL-1.0
- OPL-UK-3.0
- OPUBL-1.0
- OSET-PL-2.1
- OSL-1.0
- OSL-1.1
- OSL-2.0
- OSL-2.1
- OSL-3.0
- Parity-6.0.0
- Parity-7.0.0
- PDDL-1.0
- PHP-3.0
- PHP-3.01
- Plexus
- PolyForm-Noncommercial-1.0.0
- PolyForm-Small-Business-1.0.0
- PostgreSQL
- PSF-2.0
- psfrag
- psutils
- Python-2.0
- Python-2.0.1
- Qhull
- QPL-1.0
- QPL-1.0-INRIA-2004
- Rdisc
- RHeCos-1.1
- RPL-1.1
- RPL-1.5
- RPSL-1.0
- RSA-MD
- RSCPL
- Ruby
- SAX-PD
- Saxpath
- SCEA
- SchemeReport
- Sendmail
- Sendmail-8.23
- SGI-B-1.0
- SGI-B-1.1
- SGI-B-2.0
- SGP4
- SHL-0.5
- SHL-0.51
- SimPL-2.0
- SISSL
- SISSL-1.2
- Sleepycat
- SMLNJ
- SMPPL
- SNIA
- snprintf
- Spencer-86
- Spencer-94
- Spencer-99
- SPL-1.0
- SSH-OpenSSH
- SSH-short
- SSPL-1.0
- SugarCRM-1.1.3
- SunPro
- SWL
- Symlinks
- TAPR-OHL-1.0
- TCL
- TCP-wrappers
- TermReadKey
- TMate
- TORQUE-1.1
- TOSL
- TPDL
- TPL-1.0
- TTWL
- TU-Berlin-1.0
- TU-Berlin-2.0
- UCAR
- UCL-1.0
- Unicode-DFS-2015
- Unicode-DFS-2016
- Unicode-TOU
- UnixCrypt
- Unlicense
- UPL-1.0
- Vim
- VOSTROM
- VSL-1.0
- W3C
- W3C-19980720
- W3C-20150513
- w3m
- Watcom-1.0
- Widget-Workshop
- Wsuipa
- WTFPL
- X11
- X11-distribute-modifications-variant
- Xdebug-1.03
- Xerox
- Xfig
- XFree86-1.1
- xinetd
- xlock
- Xnet
- xpp
- XSkat
- YPL-1.0
- YPL-1.1
- Zed
- Zend-2.0
- Zimbra-1.3
- Zimbra-1.4
- Zlib
- zlib-acknowledgement
- ZPL-1.1
- ZPL-2.0
- ZPL-2.1


</details>

## `name`<sub> str</sub>
A human-readable name of this model.
It should be no longer than 64 characters
and may only contain letter, number, underscore, minus or space characters.


## `outputs`<sub> Sequence[OutputTensor]</sub>
Describes the output tensors.
<details><summary>Sequence[OutputTensor]

</summary>


OutputTensor:
### `outputs.i.name`<sub> str</sub>
Tensor name. No duplicates are allowed.


### `outputs.i.description`<sub> str</sub> = \<empty string\>
Brief descripiton of the tensor


### `outputs.i.axes`<sub> Sequence</sub>

<details><summary>Sequence[Union[BatchAxis, ChannelAxis, IndexAxis, OutputTimeAxis, OutputSpaceAxis] (discriminator=type)]

</summary>

Sequence[Union[BatchAxis, ChannelAxis, IndexAxis, OutputTimeAxis, OutputSpaceAxis] (discriminator=type)]

BatchAxis:
#### `outputs.i.axes.i.type`<sub> Literal[batch]</sub> = batch



#### `outputs.i.axes.i.name`<sub> str</sub> = batch
a unique name


#### `outputs.i.axes.i.description`<sub> str</sub> = \<empty string\>



#### `outputs.i.axes.i.size`<sub> ParametrizedBatchSize</sub> = min=1 step=1 step_with='BATCH_AXES'
The axis size.
To specify that this axis' size equals another, an axis name can be given.
Specify another tensor's axis as `<tensor name>.<axis name>`.
<details><summary>ParametrizedBatchSize

</summary>


ParametrizedBatchSize:
##### `outputs.i.axes.i.size.min`<sub> Literal[1]</sub> = 1



##### `outputs.i.axes.i.size.step`<sub> Literal[1]</sub> = 1



##### `outputs.i.axes.i.size.step_with`<sub> Literal[BATCH_AXES]</sub> = BATCH_AXES
name of another axis to resize jointly,
i.e. `n=n_other` for `size = min + n*step`, `size_other = min_other + n_other*step_other`.
To step with an axis of another tensor, use `step_with = <tensor name>.<axis name>`.
`step_with="BATCH_AXES"` is a special value to step jointly with all batch dimensions.



</details>

ChannelAxis:
#### `outputs.i.axes.i.type`<sub> Literal[channel]</sub> = channel



#### `outputs.i.axes.i.name`<sub> str</sub> = channel
a unique name


#### `outputs.i.axes.i.description`<sub> str</sub> = \<empty string\>



#### `outputs.i.axes.i.size`<sub> Union</sub> = #channel_names
The axis size.
To specify that this axis' size equals another, an axis name can be given.
Specify another tensor's axis as `<tensor name>.<axis name>`.
Union[int (Gt(gt=0)), Literal[#channel_names]]

#### `outputs.i.axes.i.channel_names`<sub> Sequence</sub>

<details><summary>Sequence[str*]

</summary>

Sequence of str
(MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))

</details>

IndexAxis:
#### `outputs.i.axes.i.type`<sub> Literal[index]</sub> = index



#### `outputs.i.axes.i.name`<sub> str</sub> = index
a unique name


#### `outputs.i.axes.i.description`<sub> str</sub> = \<empty string\>



#### `outputs.i.axes.i.size`<sub> Union</sub>
The axis size.
To specify that this axis' size equals another, an axis name can be given.
Specify another tensor's axis as `<tensor name>.<axis name>`.
<details><summary>Union[int*, ..., str*]

</summary>

Union of
- int (Gt(gt=0))
- ParametrizedSize
- SizeReference
- str
  (MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))
- str (MaxLen(max_length=33))


ParametrizedSize:
##### `outputs.i.axes.i.size.min`<sub> int</sub>



##### `outputs.i.axes.i.size.step`<sub> int</sub>



##### `outputs.i.axes.i.size.step_with`<sub> Union</sub> = None
name of another axis to resize jointly,
i.e. `n=n_other` for `size = min + n*step`, `size_other = min_other + n_other*step_other`.
To step with an axis of another tensor, use `step_with = <tensor name>.<axis name>`.
`step_with="BATCH_AXES"` is a special value to step jointly with all batch dimensions.

<details><summary>Union[str*, str*, Literal[BATCH_AXES], None]

</summary>

Union of
- str
  (MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))
- str (MaxLen(max_length=33))
- Literal[BATCH_AXES]
- None


</details>

SizeReference:
##### `outputs.i.axes.i.size.reference`<sub> Union</sub>

<details><summary>Union[str*, str*]

</summary>

Union of
- str
  (MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))
- str (MaxLen(max_length=33))


</details>

##### `outputs.i.axes.i.size.offset`<sub> int</sub> = 0



</details>

OutputTimeAxis:
#### `outputs.i.axes.i.halo`<sub> int</sub> = 0
The halo should be cropped from the output tensor to avoid boundary effects.
It is to be cropped from both sides, i.e. `size_after_crop = size - 2 * halo`.
To document a halo that is already cropped by the model use `size.offset` instead.


#### `outputs.i.axes.i.type`<sub> Literal[time]</sub> = time



#### `outputs.i.axes.i.name`<sub> str</sub> = time
a unique name


#### `outputs.i.axes.i.description`<sub> str</sub> = \<empty string\>



#### `outputs.i.axes.i.size`<sub> Union</sub>
The axis size.
To specify that this axis' size equals another, an axis name can be given.
Specify another tensor's axis as `<tensor name>.<axis name>`.
<details><summary>Union[int*, ..., str*]

</summary>

Union of
- int (Gt(gt=0))
- ParametrizedSize
- SizeReference
- str
  (MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))
- str (MaxLen(max_length=33))


ParametrizedSize:
##### `outputs.i.axes.i.size.min`<sub> int</sub>



##### `outputs.i.axes.i.size.step`<sub> int</sub>



##### `outputs.i.axes.i.size.step_with`<sub> Union</sub> = None
name of another axis to resize jointly,
i.e. `n=n_other` for `size = min + n*step`, `size_other = min_other + n_other*step_other`.
To step with an axis of another tensor, use `step_with = <tensor name>.<axis name>`.
`step_with="BATCH_AXES"` is a special value to step jointly with all batch dimensions.

<details><summary>Union[str*, str*, Literal[BATCH_AXES], None]

</summary>

Union of
- str
  (MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))
- str (MaxLen(max_length=33))
- Literal[BATCH_AXES]
- None


</details>

SizeReference:
##### `outputs.i.axes.i.size.reference`<sub> Union</sub>

<details><summary>Union[str*, str*]

</summary>

Union of
- str
  (MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))
- str (MaxLen(max_length=33))


</details>

##### `outputs.i.axes.i.size.offset`<sub> int</sub> = 0



</details>

#### `outputs.i.axes.i.unit`<sub> Optional</sub> = None

<details><summary>Optional[Literal[attosecond, ..., zettasecond]]

</summary>

Optional[Literal of
- attosecond
- centisecond
- day
- decisecond
- exasecond
- femtosecond
- gigasecond
- hectosecond
- hour
- kilosecond
- megasecond
- microsecond
- millisecond
- minute
- nanosecond
- petasecond
- picosecond
- second
- terasecond
- yoctosecond
- yottasecond
- zeptosecond
- zettasecond
]

</details>

#### `outputs.i.axes.i.scale`<sub> float</sub> = 1.0



OutputSpaceAxis:
#### `outputs.i.axes.i.halo`<sub> int</sub> = 0
The halo should be cropped from the output tensor to avoid boundary effects.
It is to be cropped from both sides, i.e. `size_after_crop = size - 2 * halo`.
To document a halo that is already cropped by the model use `size.offset` instead.


#### `outputs.i.axes.i.type`<sub> Literal[space]</sub> = space



#### `outputs.i.axes.i.name`<sub> str</sub> = x
a unique name


#### `outputs.i.axes.i.description`<sub> str</sub> = \<empty string\>



#### `outputs.i.axes.i.size`<sub> Union</sub>
The axis size.
To specify that this axis' size equals another, an axis name can be given.
Specify another tensor's axis as `<tensor name>.<axis name>`.
<details><summary>Union[int*, ..., str*]

</summary>

Union of
- int (Gt(gt=0))
- ParametrizedSize
- SizeReference
- str
  (MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))
- str (MaxLen(max_length=33))


ParametrizedSize:
##### `outputs.i.axes.i.size.min`<sub> int</sub>



##### `outputs.i.axes.i.size.step`<sub> int</sub>



##### `outputs.i.axes.i.size.step_with`<sub> Union</sub> = None
name of another axis to resize jointly,
i.e. `n=n_other` for `size = min + n*step`, `size_other = min_other + n_other*step_other`.
To step with an axis of another tensor, use `step_with = <tensor name>.<axis name>`.
`step_with="BATCH_AXES"` is a special value to step jointly with all batch dimensions.

<details><summary>Union[str*, str*, Literal[BATCH_AXES], None]

</summary>

Union of
- str
  (MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))
- str (MaxLen(max_length=33))
- Literal[BATCH_AXES]
- None


</details>

SizeReference:
##### `outputs.i.axes.i.size.reference`<sub> Union</sub>

<details><summary>Union[str*, str*]

</summary>

Union of
- str
  (MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword); MaxLen(max_length=16))
- str (MaxLen(max_length=33))


</details>

##### `outputs.i.axes.i.size.offset`<sub> int</sub> = 0



</details>

#### `outputs.i.axes.i.unit`<sub> Optional</sub> = None

<details><summary>Optional[Literal[angstrom, ..., zettameter]]

</summary>

Optional[Literal of
- angstrom
- attometer
- centimeter
- decimeter
- exameter
- femtometer
- foot
- gigameter
- hectometer
- inch
- kilometer
- megameter
- meter
- micrometer
- mile
- millimeter
- nanometer
- parsec
- petameter
- picometer
- terameter
- yard
- yoctometer
- yottameter
- zeptometer
- zettameter
]

</details>

#### `outputs.i.axes.i.scale`<sub> float</sub> = 1.0



</details>

### `outputs.i.test_tensor`<sub> Union</sub>
An example tensor to use for testing.
Using the model with the test input tensors is expected to yield the test output tensors.
Each test tensor has be a an ndarray in the
[numpy.lib file format](https://numpy.org/doc/stable/reference/generated/numpy.lib.format.html#module-numpy.lib.format).
The file extension must be '.npy'.
Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]

### `outputs.i.sample_tensor`<sub> Union</sub> = None
A sample tensor to illustrate a possible input/output for the model,
The sample files primarily serve to inform a human user about an example use case
and are typically stored as HDF5, PNG or TIFF images.
Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath, None]

### `outputs.i.values`<sub> Union</sub>
Description of tensor values, optionally per channel.
If specified per channel, `data_type` needs to match across channels for interval and ratio type values.
<details><summary>Union[Union[NominalTensorValue, OrdinalTensorValue, IntervalTensorValue, RatioTensorValue]*, Sequence[Union[NominalTensorValue, OrdinalTensorValue, IntervalTensorValue, RatioTensorValue]*]]

</summary>

Union of
- Union[NominalTensorValue, OrdinalTensorValue, IntervalTensorValue, RatioTensorValue] (discriminator=type)
- Sequence[Union[NominalTensorValue, OrdinalTensorValue, IntervalTensorValue, RatioTensorValue] (discriminator=type)]


NominalTensorValue:
#### `outputs.i.values.description`<sub> str</sub> = \<empty string\>
Brief descripiton of tensor values


#### `outputs.i.values.type`<sub> Literal[nominal]</sub> = nominal



#### `outputs.i.values.values`<sub> Sequence</sub>

Sequence[Union[int, float, str, bool]]

OrdinalTensorValue:
#### `outputs.i.values.description`<sub> str</sub> = \<empty string\>
Brief descripiton of tensor values


#### `outputs.i.values.type`<sub> Literal[ordinal]</sub> = ordinal



#### `outputs.i.values.values`<sub> Sequence</sub>
values in ascending order
Sequence[Union[int, float, str, bool]]

IntervalTensorValue:
#### `outputs.i.values.description`<sub> str</sub> = \<empty string\>
Brief descripiton of tensor values


#### `outputs.i.values.unit`<sub> Optional</sub> = None

<details><summary>Optional[str*]

</summary>

Optional[str
(None; Len(min_length=1, max_length=None); pattern='^(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^[+-]?[1-9]\\d*)?((·(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^[+-]?[1-9]\\d*)?)|(/(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^+?[1-9]\\d*)?))*$; BeforeValidator(<lambda>))]

</details>

#### `outputs.i.values.factor`<sub> float</sub> = 1.0



#### `outputs.i.values.data_type`<sub> Literal</sub>

Literal[float32, float64, uint8, int8, uint16, int16, uint32, int32, uint64, int64]

#### `outputs.i.values.data_range`<sub> Sequence</sub> = (None, None)
Tuple `(minimum, maximum)` specifying the allowed range of the data in this tensor.
`None` correspond to min/max of what can be expressed by `data_type`.
Sequence[Optional[float], Optional[float]]

#### `outputs.i.values.type`<sub> Literal[interval]</sub> = interval



RatioTensorValue:
#### `outputs.i.values.description`<sub> str</sub> = \<empty string\>
Brief descripiton of tensor values


#### `outputs.i.values.unit`<sub> Optional</sub> = None

<details><summary>Optional[str*]

</summary>

Optional[str
(None; Len(min_length=1, max_length=None); pattern='^(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^[+-]?[1-9]\\d*)?((·(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^[+-]?[1-9]\\d*)?)|(/(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^+?[1-9]\\d*)?))*$; BeforeValidator(<lambda>))]

</details>

#### `outputs.i.values.factor`<sub> float</sub> = 1.0



#### `outputs.i.values.data_type`<sub> Literal</sub>

Literal[float32, float64, uint8, int8, uint16, int16, uint32, int32, uint64, int64]

#### `outputs.i.values.data_range`<sub> Sequence</sub> = (None, None)
Tuple `(minimum, maximum)` specifying the allowed range of the data in this tensor.
`None` correspond to min/max of what can be expressed by `data_type`.
Sequence[Optional[float], Optional[float]]

#### `outputs.i.values.type`<sub> Literal[ratio]</sub> = ratio



#### `outputs.i.values.offset`<sub> float</sub> = 0.0



NominalTensorValue:
#### `outputs.i.values.i.description`<sub> str</sub> = \<empty string\>
Brief descripiton of tensor values


#### `outputs.i.values.i.type`<sub> Literal[nominal]</sub> = nominal



#### `outputs.i.values.i.values`<sub> Sequence</sub>

Sequence[Union[int, float, str, bool]]

OrdinalTensorValue:
#### `outputs.i.values.i.description`<sub> str</sub> = \<empty string\>
Brief descripiton of tensor values


#### `outputs.i.values.i.type`<sub> Literal[ordinal]</sub> = ordinal



#### `outputs.i.values.i.values`<sub> Sequence</sub>
values in ascending order
Sequence[Union[int, float, str, bool]]

IntervalTensorValue:
#### `outputs.i.values.i.description`<sub> str</sub> = \<empty string\>
Brief descripiton of tensor values


#### `outputs.i.values.i.unit`<sub> Optional</sub> = None

<details><summary>Optional[str*]

</summary>

Optional[str
(None; Len(min_length=1, max_length=None); pattern='^(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^[+-]?[1-9]\\d*)?((·(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^[+-]?[1-9]\\d*)?)|(/(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^+?[1-9]\\d*)?))*$; BeforeValidator(<lambda>))]

</details>

#### `outputs.i.values.i.factor`<sub> float</sub> = 1.0



#### `outputs.i.values.i.data_type`<sub> Literal</sub>

Literal[float32, float64, uint8, int8, uint16, int16, uint32, int32, uint64, int64]

#### `outputs.i.values.i.data_range`<sub> Sequence</sub> = (None, None)
Tuple `(minimum, maximum)` specifying the allowed range of the data in this tensor.
`None` correspond to min/max of what can be expressed by `data_type`.
Sequence[Optional[float], Optional[float]]

#### `outputs.i.values.i.type`<sub> Literal[interval]</sub> = interval



RatioTensorValue:
#### `outputs.i.values.i.description`<sub> str</sub> = \<empty string\>
Brief descripiton of tensor values


#### `outputs.i.values.i.unit`<sub> Optional</sub> = None

<details><summary>Optional[str*]

</summary>

Optional[str
(None; Len(min_length=1, max_length=None); pattern='^(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^[+-]?[1-9]\\d*)?((·(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^[+-]?[1-9]\\d*)?)|(/(Q|R|Y|Z|E|P|T|G|M|k|h|da|d|c|m|µ|n|p|f|a|z|y|r|q)?(m|g|s|A|K|mol|cd|Hz|N|Pa|J|W|C|V|F|Ω|S|Wb|T|H|lm|lx|Bq|Gy|Sv|kat|l|L)(\\^+?[1-9]\\d*)?))*$; BeforeValidator(<lambda>))]

</details>

#### `outputs.i.values.i.factor`<sub> float</sub> = 1.0



#### `outputs.i.values.i.data_type`<sub> Literal</sub>

Literal[float32, float64, uint8, int8, uint16, int16, uint32, int32, uint64, int64]

#### `outputs.i.values.i.data_range`<sub> Sequence</sub> = (None, None)
Tuple `(minimum, maximum)` specifying the allowed range of the data in this tensor.
`None` correspond to min/max of what can be expressed by `data_type`.
Sequence[Optional[float], Optional[float]]

#### `outputs.i.values.i.type`<sub> Literal[ratio]</sub> = ratio



#### `outputs.i.values.i.offset`<sub> float</sub> = 0.0



</details>

### `outputs.i.postprocessing`<sub> Sequence</sub> = ()
Description of how this output should be postprocessed.
<details><summary>Sequence[Union[model.v0_4.Binarize, ..., model.v0_4.ScaleMeanVariance]*]

</summary>

Sequence of Union of
- model.v0_4.Binarize
- model.v0_4.Clip
- model.v0_4.ScaleLinear
- model.v0_4.Sigmoid
- model.v0_4.ZeroMeanUnitVariance
- model.v0_4.ScaleRange
- model.v0_4.ScaleMeanVariance

(discriminator=name)

model.v0_4.Binarize:
#### `outputs.i.postprocessing.i.name`<sub> Literal[binarize]</sub> = binarize



#### `outputs.i.postprocessing.i.kwargs`<sub> model.v0_4.BinarizeKwargs</sub>
key word arguments
<details><summary>model.v0_4.BinarizeKwargs

</summary>


model.v0_4.BinarizeKwargs:
##### `outputs.i.postprocessing.i.kwargs.threshold`<sub> float</sub>
The fixed threshold


</details>

model.v0_4.Clip:
#### `outputs.i.postprocessing.i.name`<sub> Literal[clip]</sub> = clip



#### `outputs.i.postprocessing.i.kwargs`<sub> model.v0_4.ClipKwargs</sub>
key word arguments
<details><summary>model.v0_4.ClipKwargs

</summary>


model.v0_4.ClipKwargs:
##### `outputs.i.postprocessing.i.kwargs.min`<sub> float</sub>
minimum value for clipping


##### `outputs.i.postprocessing.i.kwargs.max`<sub> float</sub>
maximum value for clipping


</details>

model.v0_4.ScaleLinear:
#### `outputs.i.postprocessing.i.name`<sub> Literal[scale_linear]</sub> = scale_linear



#### `outputs.i.postprocessing.i.kwargs`<sub> model.v0_4.ScaleLinearKwargs</sub>
key word arguments
<details><summary>model.v0_4.ScaleLinearKwargs

</summary>


model.v0_4.ScaleLinearKwargs:
##### `outputs.i.postprocessing.i.kwargs.axes`<sub> Optional</sub> = None
The subset of axes to scale jointly.
For example xy to scale the two image axes for 2d data jointly.
Optional[str (RestrictCharacters(alphabet='czyx'); AfterValidator(validate_unique_entries))]

##### `outputs.i.postprocessing.i.kwargs.gain`<sub> Union[float, Sequence[float]]</sub> = 1.0
multiplicative factor


##### `outputs.i.postprocessing.i.kwargs.offset`<sub> Union[float, Sequence[float]]</sub> = 0.0
additive term


</details>

model.v0_4.Sigmoid:
#### `outputs.i.postprocessing.i.name`<sub> Literal[sigmoid]</sub> = sigmoid



#### `outputs.i.postprocessing.i.kwargs`<sub> model.v0_4.ProcessingKwargs</sub> =
key word arguments


model.v0_4.ZeroMeanUnitVariance:
#### `outputs.i.postprocessing.i.name`<sub> Literal[zero_mean_unit_variance]</sub> = zero_mean_unit_variance



#### `outputs.i.postprocessing.i.kwargs`<sub> model.v0_4.ZeroMeanUnitVarianceK</sub>
key word arguments
<details><summary>model.v0_4.ZeroMeanUnitVarianceKwargs

</summary>

model.v0_4.ZeroMeanUnitVarianceKwargs

model.v0_4.ZeroMeanUnitVarianceKwargs:
##### `outputs.i.postprocessing.i.kwargs.mode`<sub> Literal</sub> = fixed
Mode for computing mean and variance.
| mode | description |
| --- | ---- |
| per_dataset | mean and variance are computed for the entire dataset |
| per_sample | mean and variance are computed for each sample individually |

| fixed | fixed values for mean and variance |

Literal[fixed, per_dataset, per_sample]

##### `outputs.i.postprocessing.i.kwargs.axes`<sub> str</sub>
The subset of axes to normalize jointly.
For example `xy` to normalize the two image axes for 2d data jointly.


##### `outputs.i.postprocessing.i.kwargs.mean`<sub> Union</sub> = None
The mean value(s) to use for `mode: fixed`.
For example `[1.1, 2.2, 3.3]` in the case of a 3 channel image with `axes: xy`.
Union[float, Sequence[float] (MinLen(min_length=1)), None]

##### `outputs.i.postprocessing.i.kwargs.std`<sub> Union</sub> = None
The standard deviation values to use for `mode: fixed`. Analogous to mean.
Union[float, Sequence[float] (MinLen(min_length=1)), None]

##### `outputs.i.postprocessing.i.kwargs.eps`<sub> float</sub> = 1e-06
epsilon for numeric stability: `out = (tensor - mean) / (std + eps)`.


</details>

model.v0_4.ScaleRange:
#### `outputs.i.postprocessing.i.name`<sub> Literal[scale_range]</sub> = scale_range



#### `outputs.i.postprocessing.i.kwargs`<sub> model.v0_4.ScaleRangeKwargs</sub>
key word arguments
<details><summary>model.v0_4.ScaleRangeKwargs

</summary>


model.v0_4.ScaleRangeKwargs:
##### `outputs.i.postprocessing.i.kwargs.mode`<sub> Literal[per_dataset, per_sample]</sub>



##### `outputs.i.postprocessing.i.kwargs.axes`<sub> str</sub>
The subset of axes to normalize jointly.
For example xy to normalize the two image axes for 2d data jointly.


##### `outputs.i.postprocessing.i.kwargs.min_percentile`<sub> float</sub> = 0.0
The lower percentile used for normalization.


##### `outputs.i.postprocessing.i.kwargs.max_percentile`<sub> float</sub> = 100.0
The upper percentile used for normalization
Has to be bigger than `min_percentile`.
The range is 1 to 100 instead of 0 to 100 to avoid mistakenly
accepting percentiles specified in the range 0.0 to 1.0.


##### `outputs.i.postprocessing.i.kwargs.eps`<sub> float</sub> = 1e-06
Epsilon for numeric stability.
`out = (tensor - v_lower) / (v_upper - v_lower + eps)`;
with `v_lower,v_upper` values at the respective percentiles.


##### `outputs.i.postprocessing.i.kwargs.reference_tensor`<sub> Optional</sub> = None
Tensor name to compute the percentiles from. Default: The tensor itself.
For any tensor in `inputs` only input tensor references are allowed.
For a tensor in `outputs` only input tensor refereences are allowed if `mode: per_dataset`
<details><summary>Optional[str*]

</summary>

Optional[str
(MinLen(min_length=1); Predicate(islower); AfterValidator(validate_identifier); AfterValidator(validate_is_not_keyword))]

</details>

</details>

model.v0_4.ScaleMeanVariance:
#### `outputs.i.postprocessing.i.name`<sub> Literal[scale_mean_variance]</sub> = scale_mean_variance



#### `outputs.i.postprocessing.i.kwargs`<sub> model.v0_4.ScaleMeanVarianceKwar</sub>
key word arguments
<details><summary>model.v0_4.ScaleMeanVarianceKwargs

</summary>

model.v0_4.ScaleMeanVarianceKwargs

model.v0_4.ScaleMeanVarianceKwargs:
##### `outputs.i.postprocessing.i.kwargs.mode`<sub> Literal[per_dataset, per_sample]</sub>



##### `outputs.i.postprocessing.i.kwargs.reference_tensor`<sub> str</sub>
Name of tensor to match.


##### `outputs.i.postprocessing.i.kwargs.axes`<sub> Optional</sub> = None
The subset of axes to scale jointly.
For example xy to normalize the two image axes for 2d data jointly.
Default: scale all non-batch axes jointly.
Optional[str (RestrictCharacters(alphabet='czyx'); AfterValidator(validate_unique_entries))]

##### `outputs.i.postprocessing.i.kwargs.eps`<sub> float</sub> = 1e-06
Epsilon for numeric stability:
"`out  = (tensor - mean) / (std + eps) * (ref_std + eps) + ref_mean.


</details>

</details>

</details>

## `timestamp`<sub> datetime.datetime</sub>
Timestamp in [ISO 8601](#https://en.wikipedia.org/wiki/ISO_8601) format
with a few restrictions listed [here](https://docs.python.org/3/library/datetime.html#datetime.datetime.fromisoformat).


## `weights`<sub> Weights</sub>
The weights for this model.
Weights can be given for different formats, but should otherwise be equivalent.
The available weight formats determine which consumers can use this model.
<details><summary>Weights

</summary>


Weights:
### `weights.keras_hdf5`<sub> Optional</sub> = None

<details><summary>Optional[model.v0_4.KerasHdf5Entry]

</summary>

Optional[model.v0_4.KerasHdf5Entry]

model.v0_4.KerasHdf5Entry:
#### `weights.keras_hdf5.source`<sub> Union</sub>
∈📦 The weights file.
Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]

#### `weights.keras_hdf5.sha256`<sub> Optional</sub> = None
SHA256 checksum of the source file
You can drag and drop your file to this
[online tool](http://emn178.github.io/online-tools/sha256_checksum.html) to generate a SHA256 in your browser.
Or you can generate a SHA256 checksum with Python's `hashlib`,
[here is a codesnippet](https://gist.github.com/FynnBe/e64460463df89439cff218bbf59c1100).
Optional[str (Len(min_length=64, max_length=64))]

#### `weights.keras_hdf5.attachments`<sub> Optional</sub> = None
Attachments that are specific to this weights entry.
<details><summary>Optional[generic.v0_2.Attachments]

</summary>

Optional[generic.v0_2.Attachments]

generic.v0_2.Attachments:
##### `weights.keras_hdf5.attachments.files`<sub> Sequence</sub> = ()
∈📦 File attachments
Sequence[Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]]

</details>

#### `weights.keras_hdf5.authors`<sub> Optional</sub> = None
Authors:
If this is the initial weights entry (in other words: it does not have a `parent` field):
    the person(s) that have trained this model.
If this is a child weight (it has a `parent` field):
    the person(s) who have converted the weights to this format.

<details><summary>Optional[Sequence[generic.v0_2.Author]]

</summary>

Optional[Sequence[generic.v0_2.Author]]

generic.v0_2.Author:
##### `weights.keras_hdf5.authors.i.name`<sub> str</sub>
Full name


##### `weights.keras_hdf5.authors.i.affiliation`<sub> Optional[str]</sub> = None
Affiliation


##### `weights.keras_hdf5.authors.i.email`<sub> Optional[Email]</sub> = None
Email


##### `weights.keras_hdf5.authors.i.github_user`<sub> Optional[str]</sub> = None
GitHub user name


##### `weights.keras_hdf5.authors.i.orcid`<sub> Optional</sub> = None
An [ORCID iD](https://support.orcid.org/hc/en-us/sections/360001495313-What-is-ORCID
) in hyphenated groups of 4 digits, (and [valid](
https://support.orcid.org/hc/en-us/articles/360006897674-Structure-of-the-ORCID-Identifier
) as per ISO 7064 11,2.)

Optional[str (AfterValidator(validate_orcid_id))]

</details>

#### `weights.keras_hdf5.dependencies`<sub> Optional</sub> = None
Dependency manager and dependency file, specified as `<dependency manager>:<relative file path>`.
Optional[model.v0_4.Dependencies]

#### `weights.keras_hdf5.parent`<sub> Optional</sub> = None
The source weights these weights were converted from.
For example, if a model's weights were converted from the `pytorch_state_dict` format to `torchscript`,
The `pytorch_state_dict` weights entry has no `parent` and is the parent of the `torchscript` weights.
All weight entries except one (the initial set of weights resulting from training the model),
need to have this field.
Optional[Literal[keras_hdf5, onnx, pytorch_state_dict, tensorflow_js, tensorflow_saved_model_bundle, torchscript]]

#### `weights.keras_hdf5.type`<sub> Literal[keras_hdf5]</sub> = keras_hdf5



#### `weights.keras_hdf5.tensorflow_version`<sub> Optional</sub> = None
TensorFlow version used to create these weights
Optional[str (AfterValidator(validate_version))]

</details>

### `weights.onnx`<sub> Optional[model.v0_4.OnnxEntry]</sub> = None

<details><summary>Optional[model.v0_4.OnnxEntry]

</summary>


model.v0_4.OnnxEntry:
#### `weights.onnx.source`<sub> Union</sub>
∈📦 The weights file.
Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]

#### `weights.onnx.sha256`<sub> Optional</sub> = None
SHA256 checksum of the source file
You can drag and drop your file to this
[online tool](http://emn178.github.io/online-tools/sha256_checksum.html) to generate a SHA256 in your browser.
Or you can generate a SHA256 checksum with Python's `hashlib`,
[here is a codesnippet](https://gist.github.com/FynnBe/e64460463df89439cff218bbf59c1100).
Optional[str (Len(min_length=64, max_length=64))]

#### `weights.onnx.attachments`<sub> Optional</sub> = None
Attachments that are specific to this weights entry.
<details><summary>Optional[generic.v0_2.Attachments]

</summary>

Optional[generic.v0_2.Attachments]

generic.v0_2.Attachments:
##### `weights.onnx.attachments.files`<sub> Sequence</sub> = ()
∈📦 File attachments
Sequence[Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]]

</details>

#### `weights.onnx.authors`<sub> Optional</sub> = None
Authors:
If this is the initial weights entry (in other words: it does not have a `parent` field):
    the person(s) that have trained this model.
If this is a child weight (it has a `parent` field):
    the person(s) who have converted the weights to this format.

<details><summary>Optional[Sequence[generic.v0_2.Author]]

</summary>

Optional[Sequence[generic.v0_2.Author]]

generic.v0_2.Author:
##### `weights.onnx.authors.i.name`<sub> str</sub>
Full name


##### `weights.onnx.authors.i.affiliation`<sub> Optional[str]</sub> = None
Affiliation


##### `weights.onnx.authors.i.email`<sub> Optional[Email]</sub> = None
Email


##### `weights.onnx.authors.i.github_user`<sub> Optional[str]</sub> = None
GitHub user name


##### `weights.onnx.authors.i.orcid`<sub> Optional</sub> = None
An [ORCID iD](https://support.orcid.org/hc/en-us/sections/360001495313-What-is-ORCID
) in hyphenated groups of 4 digits, (and [valid](
https://support.orcid.org/hc/en-us/articles/360006897674-Structure-of-the-ORCID-Identifier
) as per ISO 7064 11,2.)

Optional[str (AfterValidator(validate_orcid_id))]

</details>

#### `weights.onnx.dependencies`<sub> Optional</sub> = None
Dependency manager and dependency file, specified as `<dependency manager>:<relative file path>`.
Optional[model.v0_4.Dependencies]

#### `weights.onnx.parent`<sub> Optional</sub> = None
The source weights these weights were converted from.
For example, if a model's weights were converted from the `pytorch_state_dict` format to `torchscript`,
The `pytorch_state_dict` weights entry has no `parent` and is the parent of the `torchscript` weights.
All weight entries except one (the initial set of weights resulting from training the model),
need to have this field.
Optional[Literal[keras_hdf5, onnx, pytorch_state_dict, tensorflow_js, tensorflow_saved_model_bundle, torchscript]]

#### `weights.onnx.type`<sub> Literal[onnx]</sub> = onnx



#### `weights.onnx.opset_version`<sub> Optional[int (Ge(ge=7))]</sub> = None
ONNX opset version


</details>

### `weights.pytorch_state_dict`<sub> Optional[PytorchStateDictEntry]</sub> = None

<details><summary>Optional[PytorchStateDictEntry]

</summary>


PytorchStateDictEntry:
#### `weights.pytorch_state_dict.source`<sub> Union</sub>
∈📦 The weights file.
Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]

#### `weights.pytorch_state_dict.sha256`<sub> Optional</sub> = None
SHA256 checksum of the source file
You can drag and drop your file to this
[online tool](http://emn178.github.io/online-tools/sha256_checksum.html) to generate a SHA256 in your browser.
Or you can generate a SHA256 checksum with Python's `hashlib`,
[here is a codesnippet](https://gist.github.com/FynnBe/e64460463df89439cff218bbf59c1100).
Optional[str (Len(min_length=64, max_length=64))]

#### `weights.pytorch_state_dict.attachments`<sub> Optional</sub> = None
Attachments that are specific to this weights entry.
<details><summary>Optional[generic.v0_2.Attachments]

</summary>

Optional[generic.v0_2.Attachments]

generic.v0_2.Attachments:
##### `weights.pytorch_state_dict.attachments.files`<sub> Sequence</sub> = ()
∈📦 File attachments
Sequence[Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]]

</details>

#### `weights.pytorch_state_dict.authors`<sub> Optional</sub> = None
Authors:
If this is the initial weights entry (in other words: it does not have a `parent` field):
    the person(s) that have trained this model.
If this is a child weight (it has a `parent` field):
    the person(s) who have converted the weights to this format.

<details><summary>Optional[Sequence[generic.v0_2.Author]]

</summary>

Optional[Sequence[generic.v0_2.Author]]

generic.v0_2.Author:
##### `weights.pytorch_state_dict.authors.i.name`<sub> str</sub>
Full name


##### `weights.pytorch_state_dict.authors.i.affiliation`<sub> Optional[str]</sub> = None
Affiliation


##### `weights.pytorch_state_dict.authors.i.email`<sub> Optional[Email]</sub> = None
Email


##### `weights.pytorch_state_dict.authors.i.github_user`<sub> Optional[str]</sub> = None
GitHub user name


##### `weights.pytorch_state_dict.authors.i.orcid`<sub> Optional</sub> = None
An [ORCID iD](https://support.orcid.org/hc/en-us/sections/360001495313-What-is-ORCID
) in hyphenated groups of 4 digits, (and [valid](
https://support.orcid.org/hc/en-us/articles/360006897674-Structure-of-the-ORCID-Identifier
) as per ISO 7064 11,2.)

Optional[str (AfterValidator(validate_orcid_id))]

</details>

#### `weights.pytorch_state_dict.dependencies`<sub> Optional</sub> = None
Dependency manager and dependency file, specified as `<dependency manager>:<relative file path>`.
Optional[model.v0_4.Dependencies]

#### `weights.pytorch_state_dict.parent`<sub> Optional</sub> = None
The source weights these weights were converted from.
For example, if a model's weights were converted from the `pytorch_state_dict` format to `torchscript`,
The `pytorch_state_dict` weights entry has no `parent` and is the parent of the `torchscript` weights.
All weight entries except one (the initial set of weights resulting from training the model),
need to have this field.
Optional[Literal[keras_hdf5, onnx, pytorch_state_dict, tensorflow_js, tensorflow_saved_model_bundle, torchscript]]

#### `weights.pytorch_state_dict.type`<sub> Literal[pytorch_state_dict]</sub> = pytorch_state_dict



#### `weights.pytorch_state_dict.architecture`<sub> Union</sub>

<details><summary>Union[ArchitectureFromSource, ArchitectureFromDependency]

</summary>

Union[ArchitectureFromSource, ArchitectureFromDependency]

ArchitectureFromSource:
##### `weights.pytorch_state_dict.architecture.callable`<sub> model.v0_4.CallableFromSourceFil</sub>
Callable returning a torch.nn.Module instance.
`<relative path to file>:<identifier of implementation within the file>`.
model.v0_4.CallableFromSourceFile

##### `weights.pytorch_state_dict.architecture.sha256`<sub> str</sub>
The SHA256 of the architecture source file.You can drag and drop your file to this
[online tool](http://emn178.github.io/online-tools/sha256_checksum.html) to generate a SHA256 in your browser.
Or you can generate a SHA256 checksum with Python's `hashlib`,
[here is a codesnippet](https://gist.github.com/FynnBe/e64460463df89439cff218bbf59c1100).


##### `weights.pytorch_state_dict.architecture.kwargs`<sub> Dict</sub>
key word arguments for the `callable`
Dict[str (MinLen(min_length=1)), Union[int, float, str, bool, None]]

ArchitectureFromDependency:
##### `weights.pytorch_state_dict.architecture.callable`<sub> model.v0_4.CallableFromDepencenc</sub>
callable returning a torch.nn.Module instance.
`<dependency-package>.<[dependency-module]>.<identifier>`.
model.v0_4.CallableFromDepencency

##### `weights.pytorch_state_dict.architecture.kwargs`<sub> Dict</sub>
key word arguments for the `callable`
Dict[str (MinLen(min_length=1)), Union[int, float, str, bool, None]]

</details>

#### `weights.pytorch_state_dict.pytorch_version`<sub> Optional</sub> = None
Version of the PyTorch library used.
If `depencencies` is specified it should include pytorch and the verison has to match.
(`dependencies` overrules `pytorch_version`)
Optional[str (AfterValidator(validate_version))]

</details>

### `weights.tensorflow_js`<sub> Optional</sub> = None

<details><summary>Optional[model.v0_4.TensorflowJsEntry]

</summary>

Optional[model.v0_4.TensorflowJsEntry]

model.v0_4.TensorflowJsEntry:
#### `weights.tensorflow_js.source`<sub> Union</sub>
∈📦 The multi-file weights.
All required files/folders should be a zip archive.
Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]

#### `weights.tensorflow_js.sha256`<sub> Optional</sub> = None
SHA256 checksum of the source file
You can drag and drop your file to this
[online tool](http://emn178.github.io/online-tools/sha256_checksum.html) to generate a SHA256 in your browser.
Or you can generate a SHA256 checksum with Python's `hashlib`,
[here is a codesnippet](https://gist.github.com/FynnBe/e64460463df89439cff218bbf59c1100).
Optional[str (Len(min_length=64, max_length=64))]

#### `weights.tensorflow_js.attachments`<sub> Optional</sub> = None
Attachments that are specific to this weights entry.
<details><summary>Optional[generic.v0_2.Attachments]

</summary>

Optional[generic.v0_2.Attachments]

generic.v0_2.Attachments:
##### `weights.tensorflow_js.attachments.files`<sub> Sequence</sub> = ()
∈📦 File attachments
Sequence[Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]]

</details>

#### `weights.tensorflow_js.authors`<sub> Optional</sub> = None
Authors:
If this is the initial weights entry (in other words: it does not have a `parent` field):
    the person(s) that have trained this model.
If this is a child weight (it has a `parent` field):
    the person(s) who have converted the weights to this format.

<details><summary>Optional[Sequence[generic.v0_2.Author]]

</summary>

Optional[Sequence[generic.v0_2.Author]]

generic.v0_2.Author:
##### `weights.tensorflow_js.authors.i.name`<sub> str</sub>
Full name


##### `weights.tensorflow_js.authors.i.affiliation`<sub> Optional[str]</sub> = None
Affiliation


##### `weights.tensorflow_js.authors.i.email`<sub> Optional[Email]</sub> = None
Email


##### `weights.tensorflow_js.authors.i.github_user`<sub> Optional[str]</sub> = None
GitHub user name


##### `weights.tensorflow_js.authors.i.orcid`<sub> Optional</sub> = None
An [ORCID iD](https://support.orcid.org/hc/en-us/sections/360001495313-What-is-ORCID
) in hyphenated groups of 4 digits, (and [valid](
https://support.orcid.org/hc/en-us/articles/360006897674-Structure-of-the-ORCID-Identifier
) as per ISO 7064 11,2.)

Optional[str (AfterValidator(validate_orcid_id))]

</details>

#### `weights.tensorflow_js.dependencies`<sub> Optional</sub> = None
Dependency manager and dependency file, specified as `<dependency manager>:<relative file path>`.
Optional[model.v0_4.Dependencies]

#### `weights.tensorflow_js.parent`<sub> Optional</sub> = None
The source weights these weights were converted from.
For example, if a model's weights were converted from the `pytorch_state_dict` format to `torchscript`,
The `pytorch_state_dict` weights entry has no `parent` and is the parent of the `torchscript` weights.
All weight entries except one (the initial set of weights resulting from training the model),
need to have this field.
Optional[Literal[keras_hdf5, onnx, pytorch_state_dict, tensorflow_js, tensorflow_saved_model_bundle, torchscript]]

#### `weights.tensorflow_js.type`<sub> Literal[tensorflow_js]</sub> = tensorflow_js



#### `weights.tensorflow_js.tensorflow_version`<sub> Optional</sub> = None
Version of the TensorFlow library used.
Optional[str (AfterValidator(validate_version))]

</details>

### `weights.tensorflow_saved_model_bundle`<sub> Optional</sub> = None

<details><summary>Optional[model.v0_4.TensorflowSavedModelBundleEntry]

</summary>

Optional[model.v0_4.TensorflowSavedModelBundleEntry]

model.v0_4.TensorflowSavedModelBundleEntry:
#### `weights.tensorflow_saved_model_bundle.source`<sub> Union</sub>
∈📦 The weights file.
Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]

#### `weights.tensorflow_saved_model_bundle.sha256`<sub> Optional</sub> = None
SHA256 checksum of the source file
You can drag and drop your file to this
[online tool](http://emn178.github.io/online-tools/sha256_checksum.html) to generate a SHA256 in your browser.
Or you can generate a SHA256 checksum with Python's `hashlib`,
[here is a codesnippet](https://gist.github.com/FynnBe/e64460463df89439cff218bbf59c1100).
Optional[str (Len(min_length=64, max_length=64))]

#### `weights.tensorflow_saved_model_bundle.attachments`<sub> Optional</sub> = None
Attachments that are specific to this weights entry.
<details><summary>Optional[generic.v0_2.Attachments]

</summary>

Optional[generic.v0_2.Attachments]

generic.v0_2.Attachments:
##### `weights.tensorflow_saved_model_bundle.attachments.files`<sub> Sequence</sub> = ()
∈📦 File attachments
Sequence[Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]]

</details>

#### `weights.tensorflow_saved_model_bundle.authors`<sub> Optional</sub> = None
Authors:
If this is the initial weights entry (in other words: it does not have a `parent` field):
    the person(s) that have trained this model.
If this is a child weight (it has a `parent` field):
    the person(s) who have converted the weights to this format.

<details><summary>Optional[Sequence[generic.v0_2.Author]]

</summary>

Optional[Sequence[generic.v0_2.Author]]

generic.v0_2.Author:
##### `weights.tensorflow_saved_model_bundle.authors.i.name`<sub> str</sub>
Full name


##### `weights.tensorflow_saved_model_bundle.authors.i.affiliation`<sub> Optional[str]</sub> = None
Affiliation


##### `weights.tensorflow_saved_model_bundle.authors.i.email`<sub> Optional[Email]</sub> = None
Email


##### `weights.tensorflow_saved_model_bundle.authors.i.github_user`<sub> Optional[str]</sub> = None
GitHub user name


##### `weights.tensorflow_saved_model_bundle.authors.i.orcid`<sub> Optional</sub> = None
An [ORCID iD](https://support.orcid.org/hc/en-us/sections/360001495313-What-is-ORCID
) in hyphenated groups of 4 digits, (and [valid](
https://support.orcid.org/hc/en-us/articles/360006897674-Structure-of-the-ORCID-Identifier
) as per ISO 7064 11,2.)

Optional[str (AfterValidator(validate_orcid_id))]

</details>

#### `weights.tensorflow_saved_model_bundle.dependencies`<sub> Optional</sub> = None
Dependency manager and dependency file, specified as `<dependency manager>:<relative file path>`.
Optional[model.v0_4.Dependencies]

#### `weights.tensorflow_saved_model_bundle.parent`<sub> Optional</sub> = None
The source weights these weights were converted from.
For example, if a model's weights were converted from the `pytorch_state_dict` format to `torchscript`,
The `pytorch_state_dict` weights entry has no `parent` and is the parent of the `torchscript` weights.
All weight entries except one (the initial set of weights resulting from training the model),
need to have this field.
Optional[Literal[keras_hdf5, onnx, pytorch_state_dict, tensorflow_js, tensorflow_saved_model_bundle, torchscript]]

#### `weights.tensorflow_saved_model_bundle.type`<sub> Literal</sub> = tensorflow_saved_model_bundle

Literal[tensorflow_saved_model_bundle]

#### `weights.tensorflow_saved_model_bundle.tensorflow_version`<sub> Optional</sub> = None
Version of the TensorFlow library used.
Optional[str (AfterValidator(validate_version))]

</details>

### `weights.torchscript`<sub> Optional</sub> = None

<details><summary>Optional[model.v0_4.TorchscriptEntry]

</summary>

Optional[model.v0_4.TorchscriptEntry]

model.v0_4.TorchscriptEntry:
#### `weights.torchscript.source`<sub> Union</sub>
∈📦 The weights file.
Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]

#### `weights.torchscript.sha256`<sub> Optional</sub> = None
SHA256 checksum of the source file
You can drag and drop your file to this
[online tool](http://emn178.github.io/online-tools/sha256_checksum.html) to generate a SHA256 in your browser.
Or you can generate a SHA256 checksum with Python's `hashlib`,
[here is a codesnippet](https://gist.github.com/FynnBe/e64460463df89439cff218bbf59c1100).
Optional[str (Len(min_length=64, max_length=64))]

#### `weights.torchscript.attachments`<sub> Optional</sub> = None
Attachments that are specific to this weights entry.
<details><summary>Optional[generic.v0_2.Attachments]

</summary>

Optional[generic.v0_2.Attachments]

generic.v0_2.Attachments:
##### `weights.torchscript.attachments.files`<sub> Sequence</sub> = ()
∈📦 File attachments
Sequence[Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]]

</details>

#### `weights.torchscript.authors`<sub> Optional</sub> = None
Authors:
If this is the initial weights entry (in other words: it does not have a `parent` field):
    the person(s) that have trained this model.
If this is a child weight (it has a `parent` field):
    the person(s) who have converted the weights to this format.

<details><summary>Optional[Sequence[generic.v0_2.Author]]

</summary>

Optional[Sequence[generic.v0_2.Author]]

generic.v0_2.Author:
##### `weights.torchscript.authors.i.name`<sub> str</sub>
Full name


##### `weights.torchscript.authors.i.affiliation`<sub> Optional[str]</sub> = None
Affiliation


##### `weights.torchscript.authors.i.email`<sub> Optional[Email]</sub> = None
Email


##### `weights.torchscript.authors.i.github_user`<sub> Optional[str]</sub> = None
GitHub user name


##### `weights.torchscript.authors.i.orcid`<sub> Optional</sub> = None
An [ORCID iD](https://support.orcid.org/hc/en-us/sections/360001495313-What-is-ORCID
) in hyphenated groups of 4 digits, (and [valid](
https://support.orcid.org/hc/en-us/articles/360006897674-Structure-of-the-ORCID-Identifier
) as per ISO 7064 11,2.)

Optional[str (AfterValidator(validate_orcid_id))]

</details>

#### `weights.torchscript.dependencies`<sub> Optional</sub> = None
Dependency manager and dependency file, specified as `<dependency manager>:<relative file path>`.
Optional[model.v0_4.Dependencies]

#### `weights.torchscript.parent`<sub> Optional</sub> = None
The source weights these weights were converted from.
For example, if a model's weights were converted from the `pytorch_state_dict` format to `torchscript`,
The `pytorch_state_dict` weights entry has no `parent` and is the parent of the `torchscript` weights.
All weight entries except one (the initial set of weights resulting from training the model),
need to have this field.
Optional[Literal[keras_hdf5, onnx, pytorch_state_dict, tensorflow_js, tensorflow_saved_model_bundle, torchscript]]

#### `weights.torchscript.type`<sub> Literal[torchscript]</sub> = torchscript



#### `weights.torchscript.pytorch_version`<sub> Optional</sub> = None
Version of the PyTorch library used.
Optional[str (AfterValidator(validate_version))]

</details>

</details>

## `attachments`<sub> Sequence</sub> = ()
file and other attachments
<details><summary>Sequence[generic.v0_3.Attachment]

</summary>

Sequence[generic.v0_3.Attachment]

generic.v0_3.Attachment:
### `attachments.i.source`<sub> Union</sub>
∈📦
Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]

### `attachments.i.sha256`<sub> Optional</sub> = None

Optional[str (Len(min_length=64, max_length=64))]

</details>

## `config`<sub> Optional[Dict[str, Any]]</sub> = None
A field for custom configuration that can contain any keys not present in the RDF spec.
This means you should not store, for example, a GitHub repo URL in `config` since there is a `git_repo` field.
Keys in `config` may be very specific to a tool or consumer software. To avoid conflicting definitions,
it is recommended to wrap added configuration into a sub-field named with the specific domain or tool name,
for example:
```yaml
config:
    bioimage_io:  # here is the domain name
        my_custom_key: 3837283
        another_key:
            nested: value
    imagej:       # config specific to ImageJ
        macro_dir: path/to/macro/file
```
If possible, please use [`snake_case`](https://en.wikipedia.org/wiki/Snake_case) for keys in `config`.
You may want to list linked files additionally under `attachments` to include them when packaging a resource.
(Packaging a resource means downloading/copying important linked files and creating a ZIP archive that contains
an altered rdf.yaml file with local references to the downloaded files.)


## `covers`<sub> Sequence</sub> = ()
∈📦 Cover images. Please use an image smaller than 500KB and an aspect ratio width to height of 2:1.
The supported image formats are: ('.gif', '.jpeg', '.jpg', '.png', '.svg')
<details><summary>Sequence[Union[Url*, RelativeFilePath]*]

</summary>

Sequence of Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]
(WithSuffix(suffix=('.gif', '.jpeg', '.jpg', '.png', '.svg'), case_sensitive=False))

</details>

## `documentation`<sub> Union</sub> = None
∈📦 URL or relative path to a markdown file with additional documentation.
The recommended documentation file name is `README.md`. An `.md` suffix is mandatory.
The documentation should include a '[#[#]]# Validation' (sub)section
with details on how to quantitatively validate the model on unseen data.
Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath, None]

## `git_repo`<sub> Optional[str]</sub> = None
A URL to the Git repository where the resource is being developed.


## `icon`<sub> Union</sub> = None
an icon for illustration
<details><summary>Union[Url*, RelativeFilePath, str*, None]

</summary>

Union of
- Url (max_length=2083 allowed_schemes=['http', 'https'])
- RelativeFilePath
- str (Len(min_length=1, max_length=2))
- None


</details>

## `id`<sub> Optional[str]</sub> = None
bioimage.io wide, unique identifier assigned by the
[bioimage.io collection](https://github.com/bioimage-io/collection-bioimage-io)


## `links`<sub> Sequence[str]</sub> = ()
IDs of other bioimage.io resources


## `maintainers`<sub> Sequence</sub> = ()
Maintainers of this resource.
If not specified, `authors` are maintainers and at least some of them has to specify their `github_user` name
<details><summary>Sequence[generic.v0_2.Maintainer]

</summary>

Sequence[generic.v0_2.Maintainer]

generic.v0_2.Maintainer:
### `maintainers.i.name`<sub> Optional[str]</sub> = None
Full name


### `maintainers.i.affiliation`<sub> Optional[str]</sub> = None
Affiliation


### `maintainers.i.email`<sub> Optional[Email]</sub> = None
Email


### `maintainers.i.github_user`<sub> str</sub>
GitHub user name


### `maintainers.i.orcid`<sub> Optional</sub> = None
An [ORCID iD](https://support.orcid.org/hc/en-us/sections/360001495313-What-is-ORCID
) in hyphenated groups of 4 digits, (and [valid](
https://support.orcid.org/hc/en-us/articles/360006897674-Structure-of-the-ORCID-Identifier
) as per ISO 7064 11,2.)

Optional[str (AfterValidator(validate_orcid_id))]

</details>

## `packaged_by`<sub> Sequence[generic.v0_2.Author]</sub> = ()
The persons that have packaged and uploaded this model.
Only required if those persons differ from the `authors`.
<details><summary>Sequence[generic.v0_2.Author]

</summary>


generic.v0_2.Author:
### `packaged_by.i.name`<sub> str</sub>
Full name


### `packaged_by.i.affiliation`<sub> Optional[str]</sub> = None
Affiliation


### `packaged_by.i.email`<sub> Optional[Email]</sub> = None
Email


### `packaged_by.i.github_user`<sub> Optional[str]</sub> = None
GitHub user name


### `packaged_by.i.orcid`<sub> Optional</sub> = None
An [ORCID iD](https://support.orcid.org/hc/en-us/sections/360001495313-What-is-ORCID
) in hyphenated groups of 4 digits, (and [valid](
https://support.orcid.org/hc/en-us/articles/360006897674-Structure-of-the-ORCID-Identifier
) as per ISO 7064 11,2.)

Optional[str (AfterValidator(validate_orcid_id))]

</details>

## `parent`<sub> Union</sub> = None
The model from which this model is derived, e.g. by fine-tuning the weights.
<details><summary>Union[model.v0_4.LinkedModel, ModelRdf, None]

</summary>

Union[model.v0_4.LinkedModel, ModelRdf, None]

model.v0_4.LinkedModel:
### `parent.id`<sub> str</sub>
A valid model `id` from the bioimage.io collection.


ModelRdf:
### `parent.rdf_source`<sub> Union</sub>
URL or relative path to a model RDF
Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]

### `parent.sha256`<sub> str</sub>
SHA256 checksum of the model RDF specified under `rdf_source`.


</details>

## `rdf_source`<sub> Union</sub> = None
Resource description file (RDF) source; used to keep track of where an rdf.yaml was downloaded from.
Do not set this field in a YAML file.
Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath, None]

## `root`<sub> Union[Path (Directory), Url]</sub> = .
Base path or URL for any relative paths specified in the RDF


## `run_mode`<sub> Optional[model.v0_4.RunMode]</sub> = None
Custom run mode for this model: for more complex prediction procedures like test time
data augmentation that currently cannot be expressed in the specification.
No standard run modes are defined yet.
<details><summary>Optional[model.v0_4.RunMode]

</summary>


model.v0_4.RunMode:
### `run_mode.name`<sub> Union[Literal[deepimagej], str]</sub>
Run mode name


### `run_mode.kwargs`<sub> shared.nodes.Kwargs</sub>
Run mode specific key word arguments


</details>

## `tags`<sub> Sequence[str]</sub> = ()
Associated tags


## `training_data`<sub> Union</sub> = None
The dataset used to train this model
<details><summary>Union[dataset.v0_3.LinkedDataset, dataset.v0_3.Dataset, None]

</summary>

Union[dataset.v0_3.LinkedDataset, dataset.v0_3.Dataset, None]

dataset.v0_3.LinkedDataset:
### `training_data.id`<sub> str</sub>
A valid dataset `id` from the bioimage.io collection.


dataset.v0_3.Dataset:
### `training_data.format_version`<sub> Literal[0.3.0]</sub> = 0.3.0
The format version of this resource specification
(not the `version` of the resource description)


### `training_data.name`<sub> str</sub>
A human-friendly name of the resource description


### `training_data.description`<sub> str</sub>
A string containing a brief description.


### `training_data.documentation`<sub> Optional</sub> = None
∈📦 URL or relative path to a markdown file with additional documentation.
The recommended documentation file name is `README.md`. An `.md` suffix is mandatory.
<details><summary>Optional[Union[Url*, RelativeFilePath]*]

</summary>

Optional[Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]
(WithSuffix(suffix='.md', case_sensitive=True))]

</details>

### `training_data.covers`<sub> Sequence</sub> = ()
∈📦 Cover images. Please use an image smaller than 500KB and an aspect ratio width to height of 2:1.
The supported image formats are: ('.gif', '.jpeg', '.jpg', '.png', '.svg')
<details><summary>Sequence[Union[Url*, RelativeFilePath]*]

</summary>

Sequence of Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]
(WithSuffix(suffix=('.gif', '.jpeg', '.jpg', '.png', '.svg'), case_sensitive=False))

</details>

### `training_data.id`<sub> Optional[str]</sub> = None
bioimage.io wide, unique identifier assigned by the
[bioimage.io collection](https://github.com/bioimage-io/collection-bioimage-io)


### `training_data.authors`<sub> Sequence[generic.v0_2.Author]</sub>
The authors are the creators of the RDF and the primary points of contact.
<details><summary>Sequence[generic.v0_2.Author]

</summary>


generic.v0_2.Author:
#### `training_data.authors.i.name`<sub> str</sub>
Full name


#### `training_data.authors.i.affiliation`<sub> Optional[str]</sub> = None
Affiliation


#### `training_data.authors.i.email`<sub> Optional[Email]</sub> = None
Email


#### `training_data.authors.i.github_user`<sub> Optional[str]</sub> = None
GitHub user name


#### `training_data.authors.i.orcid`<sub> Optional</sub> = None
An [ORCID iD](https://support.orcid.org/hc/en-us/sections/360001495313-What-is-ORCID
) in hyphenated groups of 4 digits, (and [valid](
https://support.orcid.org/hc/en-us/articles/360006897674-Structure-of-the-ORCID-Identifier
) as per ISO 7064 11,2.)

Optional[str (AfterValidator(validate_orcid_id))]

</details>

### `training_data.attachments`<sub> Sequence</sub> = ()
file and other attachments
<details><summary>Sequence[generic.v0_3.Attachment]

</summary>

Sequence[generic.v0_3.Attachment]

generic.v0_3.Attachment:
#### `training_data.attachments.i.source`<sub> Union</sub>
∈📦
Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath]

#### `training_data.attachments.i.sha256`<sub> Optional</sub> = None

Optional[str (Len(min_length=64, max_length=64))]

</details>

### `training_data.badges`<sub> Sequence[generic.v0_2.Badge]</sub> = ()
badges associated with this resource
<details><summary>Sequence[generic.v0_2.Badge]

</summary>


generic.v0_2.Badge:
#### `training_data.badges.i.label`<sub> str</sub>
badge label to display on hover


#### `training_data.badges.i.icon`<sub> Optional</sub> = None
badge icon
Optional[Url (max_length=2083 allowed_schemes=['http', 'https'])]

#### `training_data.badges.i.url`<sub> Url</sub>
target URL


</details>

### `training_data.cite`<sub> Sequence[generic.v0_2.CiteEntry]</sub>
citations
<details><summary>Sequence[generic.v0_2.CiteEntry]

</summary>


generic.v0_2.CiteEntry:
#### `training_data.cite.i.text`<sub> str</sub>
free text description


#### `training_data.cite.i.doi`<sub> Optional[str]</sub> = None
A digital object identifier (DOI) is the prefered citation reference.
See https://www.doi.org/ for details. (alternatively specify `url`)


#### `training_data.cite.i.url`<sub> Optional[str]</sub> = None
URL to cite (preferably specify a `doi` instead)


</details>

### `training_data.config`<sub> Optional[Dict[str, Any]]</sub> = None
A field for custom configuration that can contain any keys not present in the RDF spec.
This means you should not store, for example, a GitHub repo URL in `config` since there is a `git_repo` field.
Keys in `config` may be very specific to a tool or consumer software. To avoid conflicting definitions,
it is recommended to wrap added configuration into a sub-field named with the specific domain or tool name,
for example:
```yaml
config:
    bioimage_io:  # here is the domain name
        my_custom_key: 3837283
        another_key:
            nested: value
    imagej:       # config specific to ImageJ
        macro_dir: path/to/macro/file
```
If possible, please use [`snake_case`](https://en.wikipedia.org/wiki/Snake_case) for keys in `config`.
You may want to list linked files additionally under `attachments` to include them when packaging a resource.
(Packaging a resource means downloading/copying important linked files and creating a ZIP archive that contains
an altered rdf.yaml file with local references to the downloaded files.)


### `training_data.git_repo`<sub> Optional[str]</sub> = None
A URL to the Git repository where the resource is being developed.


### `training_data.icon`<sub> Union</sub> = None
an icon for illustration
<details><summary>Union[Url*, RelativeFilePath, str*, None]

</summary>

Union of
- Url (max_length=2083 allowed_schemes=['http', 'https'])
- RelativeFilePath
- str (Len(min_length=1, max_length=2))
- None


</details>

### `training_data.license`<sub> Union</sub>
A [SPDX license identifier](https://spdx.org/licenses/).
We do not support custom license beyond the SPDX license list, if you need that please
[open a GitHub issue](https://github.com/bioimage-io/spec-bioimage-io/issues/new/choose
) to discuss your intentions with the community.
<details><summary>Union[Literal[0BSD, ..., ZPL-2.1], Literal[AGPL-1.0, ..., wxWindows]*]

</summary>

Union of
- Literal of
  - 0BSD
  - AAL
  - Abstyles
  - AdaCore-doc
  - Adobe-2006
  - Adobe-Glyph
  - ADSL
  - AFL-1.1
  - AFL-1.2
  - AFL-2.0
  - AFL-2.1
  - AFL-3.0
  - Afmparse
  - AGPL-1.0-only
  - AGPL-1.0-or-later
  - AGPL-3.0-only
  - AGPL-3.0-or-later
  - Aladdin
  - AMDPLPA
  - AML
  - AMPAS
  - ANTLR-PD
  - ANTLR-PD-fallback
  - Apache-1.0
  - Apache-1.1
  - Apache-2.0
  - APAFML
  - APL-1.0
  - App-s2p
  - APSL-1.0
  - APSL-1.1
  - APSL-1.2
  - APSL-2.0
  - Arphic-1999
  - Artistic-1.0
  - Artistic-1.0-cl8
  - Artistic-1.0-Perl
  - Artistic-2.0
  - ASWF-Digital-Assets-1.0
  - ASWF-Digital-Assets-1.1
  - Baekmuk
  - Bahyph
  - Barr
  - Beerware
  - Bitstream-Charter
  - Bitstream-Vera
  - BitTorrent-1.0
  - BitTorrent-1.1
  - blessing
  - BlueOak-1.0.0
  - Boehm-GC
  - Borceux
  - Brian-Gladman-3-Clause
  - BSD-1-Clause
  - BSD-2-Clause
  - BSD-2-Clause-Patent
  - BSD-2-Clause-Views
  - BSD-3-Clause
  - BSD-3-Clause-Attribution
  - BSD-3-Clause-Clear
  - BSD-3-Clause-LBNL
  - BSD-3-Clause-Modification
  - BSD-3-Clause-No-Military-License
  - BSD-3-Clause-No-Nuclear-License
  - BSD-3-Clause-No-Nuclear-License-2014
  - BSD-3-Clause-No-Nuclear-Warranty
  - BSD-3-Clause-Open-MPI
  - BSD-4-Clause
  - BSD-4-Clause-Shortened
  - BSD-4-Clause-UC
  - BSD-4.3RENO
  - BSD-4.3TAHOE
  - BSD-Advertising-Acknowledgement
  - BSD-Attribution-HPND-disclaimer
  - BSD-Protection
  - BSD-Source-Code
  - BSL-1.0
  - BUSL-1.1
  - bzip2-1.0.6
  - C-UDA-1.0
  - CAL-1.0
  - CAL-1.0-Combined-Work-Exception
  - Caldera
  - CATOSL-1.1
  - CC-BY-1.0
  - CC-BY-2.0
  - CC-BY-2.5
  - CC-BY-2.5-AU
  - CC-BY-3.0
  - CC-BY-3.0-AT
  - CC-BY-3.0-DE
  - CC-BY-3.0-IGO
  - CC-BY-3.0-NL
  - CC-BY-3.0-US
  - CC-BY-4.0
  - CC-BY-NC-1.0
  - CC-BY-NC-2.0
  - CC-BY-NC-2.5
  - CC-BY-NC-3.0
  - CC-BY-NC-3.0-DE
  - CC-BY-NC-4.0
  - CC-BY-NC-ND-1.0
  - CC-BY-NC-ND-2.0
  - CC-BY-NC-ND-2.5
  - CC-BY-NC-ND-3.0
  - CC-BY-NC-ND-3.0-DE
  - CC-BY-NC-ND-3.0-IGO
  - CC-BY-NC-ND-4.0
  - CC-BY-NC-SA-1.0
  - CC-BY-NC-SA-2.0
  - CC-BY-NC-SA-2.0-DE
  - CC-BY-NC-SA-2.0-FR
  - CC-BY-NC-SA-2.0-UK
  - CC-BY-NC-SA-2.5
  - CC-BY-NC-SA-3.0
  - CC-BY-NC-SA-3.0-DE
  - CC-BY-NC-SA-3.0-IGO
  - CC-BY-NC-SA-4.0
  - CC-BY-ND-1.0
  - CC-BY-ND-2.0
  - CC-BY-ND-2.5
  - CC-BY-ND-3.0
  - CC-BY-ND-3.0-DE
  - CC-BY-ND-4.0
  - CC-BY-SA-1.0
  - CC-BY-SA-2.0
  - CC-BY-SA-2.0-UK
  - CC-BY-SA-2.1-JP
  - CC-BY-SA-2.5
  - CC-BY-SA-3.0
  - CC-BY-SA-3.0-AT
  - CC-BY-SA-3.0-DE
  - CC-BY-SA-3.0-IGO
  - CC-BY-SA-4.0
  - CC-PDDC
  - CC0-1.0
  - CDDL-1.0
  - CDDL-1.1
  - CDL-1.0
  - CDLA-Permissive-1.0
  - CDLA-Permissive-2.0
  - CDLA-Sharing-1.0
  - CECILL-1.0
  - CECILL-1.1
  - CECILL-2.0
  - CECILL-2.1
  - CECILL-B
  - CECILL-C
  - CERN-OHL-1.1
  - CERN-OHL-1.2
  - CERN-OHL-P-2.0
  - CERN-OHL-S-2.0
  - CERN-OHL-W-2.0
  - CFITSIO
  - checkmk
  - ClArtistic
  - Clips
  - CMU-Mach
  - CNRI-Jython
  - CNRI-Python
  - CNRI-Python-GPL-Compatible
  - COIL-1.0
  - Community-Spec-1.0
  - Condor-1.1
  - copyleft-next-0.3.0
  - copyleft-next-0.3.1
  - Cornell-Lossless-JPEG
  - CPAL-1.0
  - CPL-1.0
  - CPOL-1.02
  - Crossword
  - CrystalStacker
  - CUA-OPL-1.0
  - Cube
  - curl
  - D-FSL-1.0
  - diffmark
  - DL-DE-BY-2.0
  - DOC
  - Dotseqn
  - DRL-1.0
  - DSDP
  - dtoa
  - dvipdfm
  - ECL-1.0
  - ECL-2.0
  - EFL-1.0
  - EFL-2.0
  - eGenix
  - Elastic-2.0
  - Entessa
  - EPICS
  - EPL-1.0
  - EPL-2.0
  - ErlPL-1.1
  - etalab-2.0
  - EUDatagrid
  - EUPL-1.0
  - EUPL-1.1
  - EUPL-1.2
  - Eurosym
  - Fair
  - FDK-AAC
  - Frameworx-1.0
  - FreeBSD-DOC
  - FreeImage
  - FSFAP
  - FSFUL
  - FSFULLR
  - FSFULLRWD
  - FTL
  - GD
  - GFDL-1.1-invariants-only
  - GFDL-1.1-invariants-or-later
  - GFDL-1.1-no-invariants-only
  - GFDL-1.1-no-invariants-or-later
  - GFDL-1.1-only
  - GFDL-1.1-or-later
  - GFDL-1.2-invariants-only
  - GFDL-1.2-invariants-or-later
  - GFDL-1.2-no-invariants-only
  - GFDL-1.2-no-invariants-or-later
  - GFDL-1.2-only
  - GFDL-1.2-or-later
  - GFDL-1.3-invariants-only
  - GFDL-1.3-invariants-or-later
  - GFDL-1.3-no-invariants-only
  - GFDL-1.3-no-invariants-or-later
  - GFDL-1.3-only
  - GFDL-1.3-or-later
  - Giftware
  - GL2PS
  - Glide
  - Glulxe
  - GLWTPL
  - gnuplot
  - GPL-1.0-only
  - GPL-1.0-or-later
  - GPL-2.0-only
  - GPL-2.0-or-later
  - GPL-3.0-only
  - GPL-3.0-or-later
  - Graphics-Gems
  - gSOAP-1.3b
  - HaskellReport
  - Hippocratic-2.1
  - HP-1986
  - HPND
  - HPND-export-US
  - HPND-Markus-Kuhn
  - HPND-sell-variant
  - HPND-sell-variant-MIT-disclaimer
  - HTMLTIDY
  - IBM-pibs
  - ICU
  - IEC-Code-Components-EULA
  - IJG
  - IJG-short
  - ImageMagick
  - iMatix
  - Imlib2
  - Info-ZIP
  - Inner-Net-2.0
  - Intel
  - Intel-ACPI
  - Interbase-1.0
  - IPA
  - IPL-1.0
  - ISC
  - Jam
  - JasPer-2.0
  - JPL-image
  - JPNIC
  - JSON
  - Kazlib
  - Knuth-CTAN
  - LAL-1.2
  - LAL-1.3
  - Latex2e
  - Latex2e-translated-notice
  - Leptonica
  - LGPL-2.0-only
  - LGPL-2.0-or-later
  - LGPL-2.1-only
  - LGPL-2.1-or-later
  - LGPL-3.0-only
  - LGPL-3.0-or-later
  - LGPLLR
  - Libpng
  - libpng-2.0
  - libselinux-1.0
  - libtiff
  - libutil-David-Nugent
  - LiLiQ-P-1.1
  - LiLiQ-R-1.1
  - LiLiQ-Rplus-1.1
  - Linux-man-pages-1-para
  - Linux-man-pages-copyleft
  - Linux-man-pages-copyleft-2-para
  - Linux-man-pages-copyleft-var
  - Linux-OpenIB
  - LOOP
  - LPL-1.0
  - LPL-1.02
  - LPPL-1.0
  - LPPL-1.1
  - LPPL-1.2
  - LPPL-1.3a
  - LPPL-1.3c
  - LZMA-SDK-9.11-to-9.20
  - LZMA-SDK-9.22
  - MakeIndex
  - Martin-Birgmeier
  - metamail
  - Minpack
  - MirOS
  - MIT
  - MIT-0
  - MIT-advertising
  - MIT-CMU
  - MIT-enna
  - MIT-feh
  - MIT-Festival
  - MIT-Modern-Variant
  - MIT-open-group
  - MIT-Wu
  - MITNFA
  - Motosoto
  - mpi-permissive
  - mpich2
  - MPL-1.0
  - MPL-1.1
  - MPL-2.0
  - MPL-2.0-no-copyleft-exception
  - mplus
  - MS-LPL
  - MS-PL
  - MS-RL
  - MTLL
  - MulanPSL-1.0
  - MulanPSL-2.0
  - Multics
  - Mup
  - NAIST-2003
  - NASA-1.3
  - Naumen
  - NBPL-1.0
  - NCGL-UK-2.0
  - NCSA
  - Net-SNMP
  - NetCDF
  - Newsletr
  - NGPL
  - NICTA-1.0
  - NIST-PD
  - NIST-PD-fallback
  - NIST-Software
  - NLOD-1.0
  - NLOD-2.0
  - NLPL
  - Nokia
  - NOSL
  - Noweb
  - NPL-1.0
  - NPL-1.1
  - NPOSL-3.0
  - NRL
  - NTP
  - NTP-0
  - O-UDA-1.0
  - OCCT-PL
  - OCLC-2.0
  - ODbL-1.0
  - ODC-By-1.0
  - OFFIS
  - OFL-1.0
  - OFL-1.0-no-RFN
  - OFL-1.0-RFN
  - OFL-1.1
  - OFL-1.1-no-RFN
  - OFL-1.1-RFN
  - OGC-1.0
  - OGDL-Taiwan-1.0
  - OGL-Canada-2.0
  - OGL-UK-1.0
  - OGL-UK-2.0
  - OGL-UK-3.0
  - OGTSL
  - OLDAP-1.1
  - OLDAP-1.2
  - OLDAP-1.3
  - OLDAP-1.4
  - OLDAP-2.0
  - OLDAP-2.0.1
  - OLDAP-2.1
  - OLDAP-2.2
  - OLDAP-2.2.1
  - OLDAP-2.2.2
  - OLDAP-2.3
  - OLDAP-2.4
  - OLDAP-2.5
  - OLDAP-2.6
  - OLDAP-2.7
  - OLDAP-2.8
  - OLFL-1.3
  - OML
  - OpenPBS-2.3
  - OpenSSL
  - OPL-1.0
  - OPL-UK-3.0
  - OPUBL-1.0
  - OSET-PL-2.1
  - OSL-1.0
  - OSL-1.1
  - OSL-2.0
  - OSL-2.1
  - OSL-3.0
  - Parity-6.0.0
  - Parity-7.0.0
  - PDDL-1.0
  - PHP-3.0
  - PHP-3.01
  - Plexus
  - PolyForm-Noncommercial-1.0.0
  - PolyForm-Small-Business-1.0.0
  - PostgreSQL
  - PSF-2.0
  - psfrag
  - psutils
  - Python-2.0
  - Python-2.0.1
  - Qhull
  - QPL-1.0
  - QPL-1.0-INRIA-2004
  - Rdisc
  - RHeCos-1.1
  - RPL-1.1
  - RPL-1.5
  - RPSL-1.0
  - RSA-MD
  - RSCPL
  - Ruby
  - SAX-PD
  - Saxpath
  - SCEA
  - SchemeReport
  - Sendmail
  - Sendmail-8.23
  - SGI-B-1.0
  - SGI-B-1.1
  - SGI-B-2.0
  - SGP4
  - SHL-0.5
  - SHL-0.51
  - SimPL-2.0
  - SISSL
  - SISSL-1.2
  - Sleepycat
  - SMLNJ
  - SMPPL
  - SNIA
  - snprintf
  - Spencer-86
  - Spencer-94
  - Spencer-99
  - SPL-1.0
  - SSH-OpenSSH
  - SSH-short
  - SSPL-1.0
  - SugarCRM-1.1.3
  - SunPro
  - SWL
  - Symlinks
  - TAPR-OHL-1.0
  - TCL
  - TCP-wrappers
  - TermReadKey
  - TMate
  - TORQUE-1.1
  - TOSL
  - TPDL
  - TPL-1.0
  - TTWL
  - TU-Berlin-1.0
  - TU-Berlin-2.0
  - UCAR
  - UCL-1.0
  - Unicode-DFS-2015
  - Unicode-DFS-2016
  - Unicode-TOU
  - UnixCrypt
  - Unlicense
  - UPL-1.0
  - Vim
  - VOSTROM
  - VSL-1.0
  - W3C
  - W3C-19980720
  - W3C-20150513
  - w3m
  - Watcom-1.0
  - Widget-Workshop
  - Wsuipa
  - WTFPL
  - X11
  - X11-distribute-modifications-variant
  - Xdebug-1.03
  - Xerox
  - Xfig
  - XFree86-1.1
  - xinetd
  - xlock
  - Xnet
  - xpp
  - XSkat
  - YPL-1.0
  - YPL-1.1
  - Zed
  - Zend-2.0
  - Zimbra-1.3
  - Zimbra-1.4
  - Zlib
  - zlib-acknowledgement
  - ZPL-1.1
  - ZPL-2.0
  - ZPL-2.1

- Literal of
  - AGPL-1.0
  - AGPL-3.0
  - BSD-2-Clause-FreeBSD
  - BSD-2-Clause-NetBSD
  - bzip2-1.0.5
  - eCos-2.0
  - GFDL-1.1
  - GFDL-1.2
  - GFDL-1.3
  - GPL-1.0
  - GPL-1.0+
  - GPL-2.0
  - GPL-2.0+
  - GPL-2.0-with-autoconf-exception
  - GPL-2.0-with-bison-exception
  - GPL-2.0-with-classpath-exception
  - GPL-2.0-with-font-exception
  - GPL-2.0-with-GCC-exception
  - GPL-3.0
  - GPL-3.0+
  - GPL-3.0-with-autoconf-exception
  - GPL-3.0-with-GCC-exception
  - LGPL-2.0
  - LGPL-2.0+
  - LGPL-2.1
  - LGPL-2.1+
  - LGPL-3.0
  - LGPL-3.0+
  - Nunit
  - StandardML-NJ
  - wxWindows

  (deprecated)


</details>

### `training_data.links`<sub> Sequence[str]</sub> = ()
IDs of other bioimage.io resources


### `training_data.maintainers`<sub> Sequence</sub> = ()
Maintainers of this resource.
If not specified, `authors` are maintainers and at least some of them has to specify their `github_user` name
<details><summary>Sequence[generic.v0_2.Maintainer]

</summary>

Sequence[generic.v0_2.Maintainer]

generic.v0_2.Maintainer:
#### `training_data.maintainers.i.name`<sub> Optional[str]</sub> = None
Full name


#### `training_data.maintainers.i.affiliation`<sub> Optional[str]</sub> = None
Affiliation


#### `training_data.maintainers.i.email`<sub> Optional[Email]</sub> = None
Email


#### `training_data.maintainers.i.github_user`<sub> str</sub>
GitHub user name


#### `training_data.maintainers.i.orcid`<sub> Optional</sub> = None
An [ORCID iD](https://support.orcid.org/hc/en-us/sections/360001495313-What-is-ORCID
) in hyphenated groups of 4 digits, (and [valid](
https://support.orcid.org/hc/en-us/articles/360006897674-Structure-of-the-ORCID-Identifier
) as per ISO 7064 11,2.)

Optional[str (AfterValidator(validate_orcid_id))]

</details>

### `training_data.rdf_source`<sub> Union</sub> = None
Resource description file (RDF) source; used to keep track of where an rdf.yaml was downloaded from.
Do not set this field in a YAML file.
Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath, None]

### `training_data.root`<sub> Union[Path (Directory), Url]</sub> = .
Base path or URL for any relative paths specified in the RDF


### `training_data.tags`<sub> Sequence[str]</sub> = ()
Associated tags


### `training_data.version`<sub> Optional</sub> = None
The version number of the resource. Its format must be a string in
`MAJOR.MINOR.PATCH` format following the guidelines in Semantic Versioning 2.0.0 (see https://semver.org/).
Hyphens and plus signs are not allowed to be compatible with
https://packaging.pypa.io/en/stable/version.html.
The initial version should be `"0.1.0"`.
Optional[str (AfterValidator(validate_version))]

### `training_data.source`<sub> Union</sub> = None
URL or relative path to the source of the resource
Union[Url (max_length=2083 allowed_schemes=['http', 'https']), RelativeFilePath, None]

### `training_data.type`<sub> Literal[dataset]</sub> = dataset



</details>

## `version`<sub> Optional</sub> = None
The version number of the resource. Its format must be a string in
`MAJOR.MINOR.PATCH` format following the guidelines in Semantic Versioning 2.0.0 (see https://semver.org/).
Hyphens and plus signs are not allowed to be compatible with
https://packaging.pypa.io/en/stable/version.html.
The initial version should be `"0.1.0"`.
Optional[str (AfterValidator(validate_version))]


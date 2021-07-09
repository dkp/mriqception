MODALITY_TYPES = ['bold', 't1w', 't2w']

def build_query (options):
  """
  Build a query string for the MRIQC Web API using the parameters
  given in the options dictionary.
  """
  url = set_modality(options)
  set_magnetic_field_strength(options, url)
  set_manufacturer(options, url)
  set_multiband_accel_factor(options, url)
  set_repetition_time(options, url)


def set_modality (options):
  """
  Creates and returns initial URL string with required modality (bold, T1w, or T2w).
  Raise TypeError if modality type is not specified. 
  """
  modality = options.get('modality')
  if (modality is None):
    raise TypeError("Error: required Modality type (bold, T1w, T2w) not specified.")
  else:
    modality = modality.lower()
  
  if (not modality in MODALITY_TYPES):
    raise ValueError("Error: required Modality type (bold, T1w, T2w) not specified.")
  
  return f"https://mriqc.nimh.nih.gov/api/v1/{modality}"




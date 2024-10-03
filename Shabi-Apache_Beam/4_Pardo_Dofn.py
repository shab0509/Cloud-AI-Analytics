import apache_beam as beam

class SplitRow(beam.DoFn):
  def process(self, element):
    return [element.split(',')]


class ComputeWordLengthFn(beam.DoFn):
  def process(self, element):
    return [len(element)]
  
with beam.Pipeline() as pipeline:
  input_data = (pipeline
                | "read from text">> beam.io.ReadFromText("/Users/shabivictor/Desktop/Dataflow/d1.csv", skip_header_lines= True)
                | "spliting the record" >> beam.ParDo(SplitRow()))
  
''''''
  count_data = (input_data
                |"filtering the data with PASS" >> beam.Filter(lambda record : record[5]=="FAIL"))
  
  word_lengths = (count_data 
                 |"countof records" >> beam.ParDo(ComputeWordLengthFn())
                 |beam.Map(print))
  
  output_data = (count_data
                 | "Write to Text" >> beam.io.WriteToText("result/fail_data"))

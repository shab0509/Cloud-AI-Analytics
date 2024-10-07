import apache_beam as beam 

p1= beam.Pipeline()
data_001      = (p1
           | "Read from Text" >> beam.io.ReadFromText("gs://files_0001/d1.csv", skip_header_lines=1)
           | "split the record" >> beam.Map(lambda record: record.split(','))
           #| 'Filter regular' >> beam.Filter(lambda record: record[3] == 'Tennessee')
           | 'Printing out' >> beam.Map(print)
           | 'Write to text'>> beam.io.WriteToText('gs://output_0001/d2.csv'))

p1.run()
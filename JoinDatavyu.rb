
# Import data from plaintext file.
## Params
input_file = :stream #:prompt #'~/Desktop/data.csv'
col_sep = ','
csv_opts = {
  :col_sep => col_sep
}
start_row = 1 # Row to start reading data from; first line is row 1 (use 2 to skip reading header if present)

# Denote how columns from the input file will be represented in the datavyu spreadsheet
# This is a nested associative array.
# The outer key is the name of column.
# The inner keys are names of codes, and the values for the inner keys are the indices of input
# columns containing the values for the code. The first column of the input is column 1.
code_map = {
  'transcript' => {
    'onset' => 1,
    'offset' => 2,
    'word' => 3
  }
}
# Parameters for calling python transcription library to do on-line transcription.
PY_SCRIPT_PATH = '~/SpeechRecognition_GoogleCloud_Ruby.py' #'~/GetTranscriptUser.py'

## Body
require 'Datavyu_API.rb'
require 'csv'

begin
  if(input_file == :prompt)
    # If input_file is :prompt, open up a file chooser window to let user select input file.
    java_import javax::swing::JFileChooser
    java_import javax::swing::filechooser::FileNameExtensionFilter

    txtFilter = FileNameExtensionFilter.new('Text file','txt')
    csvFilter = FileNameExtensionFilter.new('CSV file', 'csv')
    jfc = JFileChooser.new()
    jfc.setAcceptAllFileFilterUsed(false)
    jfc.setFileFilter(csvFilter)
    jfc.addChoosableFileFilter(txtFilter)
    jfc.setMultiSelectionEnabled(false)
    jfc.setDialogTitle('Select transcript text file.')

    ret = jfc.showOpenDialog(javax.swing.JPanel.new())

    if ret != JFileChooser::APPROVE_OPTION
      puts "Invalid selection. Aborting."
      return
    end
    scriptFile = jfc.getSelectedFile()
    fn = scriptFile.getAbsolutePath()
    infile = File.open(fn, 'r')
  elsif(input_file == :stream)
    # For :stream input, call the python library and pass it the first video in the Datavyu Controller.
    # Show a confirmation dialog box to the user before proceeding.
    java_import javax::swing::JOptionPane

    videos = Datavyu.getVideoController().getStreamViewers()
    if videos.empty?
      puts "There are no videos in this spreadsheet! Please add a video and run again."
      exit 1
    else
      video_path = videos.toArray().first.getSourceFile().getPath()
    end

    msg = sprintf("Confirm transcription of following file: %s\n", video_path)
    jop = JOptionPane.showConfirmDialog(nil, msg, "Proceed?", JOptionPane::YES_NO_OPTION)
    
    if jop == 0
      data = `python #{PY_SCRIPT_PATH} #{video_path}`.split("\n")
      unless $?.exitstatus == 0
        puts "Transcription unsuccessful. Exit status: #{$?}"
        exit $?.exitstatus
      end
      p data
    else
      puts "User cancelled."
      exit 0
    end

  else
    # Open input file for read
    infile = File.open(File.expand_path(input_file), 'r')
    data = infile.readlines()
  end

  # Set up spreadsheet with columns from code_map
  columns = {}
  code_map.each_pair do |column_name, pairs|
    codes = pairs.keys
    columns[column_name] = createVariable(column_name, *(codes - ['ordinal', 'onset', 'offset']))
  end

  # Init struct to keep track of data
  prev_data = {}
  code_map.keys.each{ |x| prev_data[x] = nil }

  # Read lines from the input file and add data
  data.each_with_index do |line, idx|
    next unless idx >= (start_row - 1)
    puts line
    tokens = CSV.parse_line(line, csv_opts)

    # Group data by column
    current_data = {}
    code_map.each_pair do |column_name, pairs|
      values = pairs.values.map{ |i| tokens[i-1] }
      current_data[column_name] = values

      # Make new cell if current data does not match previous data
      unless (values == prev_data[column_name]) || values.all?{ |x| x.nil? }
        ncell = columns[column_name].make_new_cell
        pairs.each_pair do |c, i|
          value = tokens[i-1]
          value = value.to_i if %w(ordinal onset offset).include?(c) # convert to int for ordinal, onset, offset values
          ncell.change_code(c, value)
        end
      end
    end

    prev_data = current_data
  end

  columns.values.each{ |x| set_column(x) }
end

# Examples

## As0

NOTE: This README comes directly from the Repp repository.  This example was adapted as a test case for PCADA.

The `As0.output.json` file was created with the following command:

This is very similar to the command executed by the PCADA application for generating designs.  Instead of using the
twist.yaml, the config<x>.yaml was used instead, but the same base input sequence was used to verify the results make
sense and it was possible to obtain different results from Repp through modifying the configuration files.

```bash
repp make seq -i As0.input.fa -o As0.output.json --addgene --settings twist.yaml -v
```

Which approximates to asking REPP to:

- make a plasmid sequence that's in `As0.input.fa`
- output build instructions in JSON to `As0.output.json`
- use source fragments from Addgene
- use synthesis settings from `twist.yaml`
- be verbose during the build

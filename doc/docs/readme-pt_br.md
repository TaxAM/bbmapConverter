# BBMap Converter

- [en](./../../readme.md)

Mapping Converter é um módulo do projeto [TaxAM](https://github.com/TaxAM/taxam) criado para transformar arquivos Mapping gerados pelo Software [BBMap](https://jgi.doe.gov/data-and-tools/software-tools/bbtools/bb-tools-user-guide/bbmap-guide/):

Ele irá transformar um arquivo em um formato
```
@HD	VN:1.4	SO:unsorted
@SQ	SN:NC_004718.3	LN:29751
@SQ	SN:NC_009452.1	LN:23814
@SQ	SN:NC_014373.1	LN:18940
@SQ	SN:NC_043439.1	LN:11916
@SQ	SN:NC_055325.1	LN:6406
@SQ	SN:NC_055508.1	LN:15270
@PG	ID:BBMap	PN:BBMap	VN:38.94	CL:java -ea -Xmx1871m -Xms1871m align2.BBMap build=1 overwrite=true fastareadlen=500 in=/data/viruses_data_01/final_sg.fa out=/data/viruses_data_01/mapping_01.txt ref=/data/viruses_data_01/contigs.fa
read_201	0	NC_014373.1	9665	43	75=	*	0	0	TTAATCACTTATATTGTATTCATTTGAAATTACTCATTAGGCAAATACTTTGATTAAGAAAAAATAATTGGAAAA	*	NM:i:0	AM:i:43
read_202	16	NC_009452.1	19020	43	75=	*	0	0	ACTGGTTAGTATTAGATGCTATCCTACACACTAGATCATTCATAGAAGCAATTGATTTCCTAGTTAACAATCCAC	*	NM:i:0	AM:i:43
read_203	0	NC_055325.1	2562	43	75=	*	0	0	CCTTGAGAGATTGGCGACATTAAAGGCCACAAGTAACTTCAATAATGGATGGTATAACTATAAGGAAGTAAAAGA	*	NM:i:0	AM:i:43
read_204	16	NC_014373.1	2079	43	75=	*	0	0	TGCCACAAGTACAGGACAGATCCGAAAATCATGACCAAACCCTTCAAACACAGTCCAGGGTTTTGACTCCTATCA	*	NM:i:0	AM:i:43
read_205	0	NC_004718.3	26316	43	75=	*	0	0	CTTCTGAAGGAGTTCCTGATCTTCTGGTCTAAACGAACTAACTATTATTATTATTCTGTTTGGAACTTTAACATT	*	NM:i:0	AM:i:43
```
para:
```
read_201    NC_014373.1
read_202    NC_009452.1
read_203    NC_055325.1
read_204    NC_014373.1
read_205    NC_004718.3
```

## Exmemplo de utilização:

```
python mappingConverter -mp "/samples/bbmap/" -op "fileCoverted"
```

Parsers:

- `-mp` : Pasta onde estão os arquivos a serem convertidos.
- `-op` : Nome dos arquivos finais. Se essa flag não for informada, o programa irá usar os nomes dos arquivos originais para criar esses nomes.
- `-ms` : Separador usado entre os itens de cada linha a ser convertidada.
- `-os` : Separador usado entre os itens de cada linha dos arquivos convertidos.

Os arquivos convertidos serão armazenados em uma paste chamada `/output_converter/` dentro da pasta `/mappingConverter/`.
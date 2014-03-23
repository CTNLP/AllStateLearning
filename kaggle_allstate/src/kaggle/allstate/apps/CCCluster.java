/**
 * 
 */
package kaggle.allstate.apps;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Set;
import kaggle.allstate.clustering.ChineseWhispers;
import kaggle.allstate.datastructures.DataSet;
import kaggle.allstate.datastructures.SingleCostumer;

/**
 * @author Christoph Teichmann
 * created Mar 23, 2014 8:06:38 PM
 * @version 0.1
 */
public class CCCluster
{
	/**
	 *
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException
	{
		BufferedReader br = new BufferedReader(new FileReader(args[0]));
		DataSet bs = new DataSet(br);
		br.close();
		double[][] weights = new double[20][30];
		for(double[] w : weights)
		{Arrays.fill(w, 1.0);}
		double[][] es = new double[20][30];
		for(double[] e : es)
		{Arrays.fill(e, 1.0);}
		ChineseWhispers cw = new ChineseWhispers(10, 100, weights, es);
		ArrayList<Set<SingleCostumer>> list = cw.cluster(bs);
		int number = 0;
		for(Set<SingleCostumer> s : list)
		{
			BufferedWriter bw = new BufferedWriter(new FileWriter(args[1]+"_"+(++number)+"txt"));
			boolean first = true;
			for(SingleCostumer sc : s)
			{
				if(first)
				{first = false;}
				else
				{bw.newLine();}
				bw.write(sc.toString());
			}
			bw.close();
		}
	}
}

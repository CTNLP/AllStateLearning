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
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.TreeMap;
/**
 * @author Christoph Teichmann
 * created Mar 12, 2014 2:40:41 PM
 * @version 0.1
 */
public class ShowAllValues
{
	public static void main(String... args) throws IOException
	{
		BufferedReader br = new BufferedReader(new FileReader(args[0]));
		String line;
		Map<String,ArrayList<Map<String,Integer>>> counts = new HashMap<>();
		String[] header = br.readLine().trim().split(",");
		int l = 0;
		while((line = br.readLine()) != null)
		{
			line  = line.trim();
			String[] parts = line.split(",");
			String point = "same";
			ArrayList<Map<String,Integer>> data = counts.get(point);
			if(data == null)
			{counts.put(point, data = new ArrayList<>());}
			while(data.size() < parts.length)
			{data.add(new HashMap<String,Integer>());}
			for(int i=0;i<parts.length;++i)
			{addOne(data.get(i),parts[i]);}
			if(parts.length != header.length)
			{
				System.out.println(Arrays.toString(header));
				System.out.println(Arrays.toString(parts));
				throw new IllegalStateException();
			}
			++l;
			if(l%1000 == 0)
			{System.out.println("read line " + (l));}
		}
		br.close();
		for(Entry<String, ArrayList<Map<String, Integer>>> ent : counts.entrySet())
		{
			String point = ent.getKey();
			ArrayList<Map<String,Integer>> data = ent.getValue();
			for(int i=0;i<data.size();++i)
			{
				BufferedWriter bw = new BufferedWriter(new FileWriter(args[1]+"_"+point+"_"+header[i]+".txt"));
				TreeMap<Integer,ArrayList<String>> list = sort(data.get(i));
				bw.write(header[i]+": ");
				for(Map.Entry<Integer, ArrayList<String>> p : list.descendingMap().entrySet())
				{
					bw.newLine();
					bw.write(p.toString());
				}
				bw.close();
			}
		}
	}
	/**
	 *
	 * @param map
	 * @return
	 */
	private static TreeMap<Integer, ArrayList<String>> sort(
			Map<String, Integer> map)
	{
		TreeMap<Integer,ArrayList<String>> ret = new TreeMap<>();
		for(Map.Entry<String, Integer> pair : map.entrySet())
		{
			ArrayList<String> vals = ret.get(pair.getValue());
			if(vals == null)
			{ret.put(pair.getValue(), vals = new ArrayList<>());}
			vals.add(pair.getKey());
		}
		return ret;
	}
	/**
	 *
	 * @param map
	 * @param string
	 */
	private static void addOne(Map<String, Integer> map, String string)
	{
		Integer val = map.get(string);
		map.put(string, val == null ? 1 : val+1);
	}
}
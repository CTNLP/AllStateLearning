/**
 * 
 */
package kaggle.allstate.datastructures;
import it.unimi.dsi.fastutil.ints.Int2ObjectOpenHashMap;
import it.unimi.dsi.fastutil.ints.IntIterator;
import java.io.BufferedReader;
import java.io.IOException;
/**
 * @author Christoph Teichmann
 * created Mar 22, 2014 5:37:49 PM
 * @version 0.1
 */
public class DataSet
{
	/**
	 * 
	 */
	private final Int2ObjectOpenHashMap<SingleCostumer>  data = new Int2ObjectOpenHashMap<>();
	/**
	 * 
	 * @param input
	 */
	public DataSet(BufferedReader input) throws IOException
	{
		input.readLine();
		String line;
		while((line = input.readLine()) != null)
		{
			String[] parts = line.trim().split(",");
			int num = Integer.parseInt(parts[0].trim());
			SingleCostumer sc = this.get(num);
			if(sc == null)
			{
				sc = new SingleCostumer(parts);
				this.data.put(Integer.parseInt(sc.getCostumer_ID()),sc);
			}
			sc.addEntry(parts);
		}
	}
	/**
	 *
	 * @param num
	 * @return
	 */
	public SingleCostumer get(int num)
	{
		if(num < 0 || num >= this.data.size())
		{return null;}
		return this.data.get(num);
	}
	/**
	 *
	 * @return
	 */
	public IntIterator getIntIterator()
	{return this.data.keySet().iterator();}
}
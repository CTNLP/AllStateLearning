/**
 * 
 */
package kaggle.allstate.datastructures;
import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;
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
	private final ArrayList<SingleCostumer>  data = new ArrayList<>();
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
				while(data.size() <= num)
				{data.add(null);}
				sc = new SingleCostumer(parts);
				this.data.add(sc);
			}
			sc.addEntry(parts);
		}
	}
	/**
	 *
	 * @param num
	 * @return
	 */
	private SingleCostumer get(int num)
	{
		if(num < 0 || num >= this.data.size())
		{return null;}
		return this.data.get(num);
	}
}
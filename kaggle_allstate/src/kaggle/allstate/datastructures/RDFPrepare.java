/**
 * 
 */
package kaggle.allstate.datastructures;
import java.util.Arrays;
/**
 * @author Christoph Teichmann
 * created Mar 22, 2014 10:21:31 PM
 * @version 0.1
 */
public class RDFPrepare
{
	/**
	 * 
	 */
	private final double[] weights = new double[22];
	{Arrays.fill(weights, 1.0);}
	/**
	 * 
	 */
	private final double[] es = new double[22];
	{Arrays.fill(es, 1.0);}
	/**
	 * 
	 *
	 * @param w
	 */
	public void setDayWeight(double w)
	{this.weights[0] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setDayE(double e)
	{this.es[0] = e;}
	/**
	 * 
	 *
	 * @param w
	 */
	public void setTimeWeight(double w)
	{this.weights[1] = w;}
	/**
	 * 
	 *
	 * @param e
	 */
	public void setTimeE(double e)
	{this.es[1] = e;}
}
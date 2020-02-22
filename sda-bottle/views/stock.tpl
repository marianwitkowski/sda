
<h2>{{ ticker }}</h2>
<table>
 <tr>
  <td width="150">data</td>
  <td width="150">Kurs</td>
  <td width="150">Wolumen</td>
   </tr>

% for key, value in stockdata.items():
    <tr>
     <td>{{ key }}</td>
     <td>{{ value[0] }}</td>
     <td>{{ value[1] }}</td>

    </tr>
%end



</table>
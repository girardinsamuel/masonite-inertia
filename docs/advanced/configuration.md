# Configuration

The package can be configured via `config/inertia.py` configuration file.

<table>
  <thead>
    <tr>
      <th style="text-align:left">Variable</th>
      <th style="text-align:left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align:left"><code>PUBLIC_PATH</code>
      </td>
      <td style="text-align:left">
        <p>Absolute path to mix-manifest.json location. It&apos;s needed for computing
          js assets version.</p>
        <p>Default: <code>project root</code>
        </p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><code>ROOT_VIEW</code>
      </td>
      <td style="text-align:left">
        <p>Global root template view used by your Inertia Controllers to render the
          page. Specify the name of the view without <code>.html</code>. See <a href="root-view.md#global-configuration">Root view</a>.</p>
        <p>Default: <code>&quot;app&quot;</code>
        </p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><code>INCLUDE_ROUTES</code>
      </td>
      <td style="text-align:left">
        <p>Include server-side routes as JSON payload in Inertia response (as a prop).
          See <a href="../the-basics/routing.md#generated-as-json-and-include-in-view">routing</a>.</p>
        <p>Default: <code>False</code>
        </p>
      </td>
    </tr>
    <tr>
      <td style="text-align:left"><code>INCLUDE_FLASH_MESSAGES</code>
      </td>
      <td style="text-align:left">
        <p>Include flash messages as JSON payload in Inertia response (as a prop).</p>
        <p>Default: <code>True</code>
        </p>
      </td>
    </tr>
  </tbody>
</table>




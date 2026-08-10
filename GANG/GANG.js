export async function GANG_SYSTEM() {

  const folders = [
    "GANG",
    "HESS",
    "eco",
    "expand",
    "grid",
    "link",
    "dezi"
  ];

  const system = {
    root: null,
    chain: [],
    files: [],
    errors: [],
    status: "INIT"
  };

  // ------------------------------------------------------
  // ROOT LADEN
  // ------------------------------------------------------
  try {
    const root = await import("./GANG.root.js");
    system.root = root.ROOT || "NO_ROOT";
  } catch (err) {
    system.errors.push("ROOT fehlt: " + err);
  }

  // ------------------------------------------------------
  // ORDNER + agent.js LADEN
  // ------------------------------------------------------
  for (const folder of folders) {
    try {
      const mod = await import(`./${folder}/agent.js`);
      system.chain.push({
        folder,
        status: "OK",
        agent: mod.agent || "NO_AGENT"
      });
    } catch (err) {
      system.chain.push({
        folder,
        status: "ERR",
        agent: null
      });
      system.errors.push(`Fehler in ${folder}/agent.js: ${err}`);
    }
  }

  // ------------------------------------------------------
  // DATEIEN SCANNEN (Diagnose)
  // ------------------------------------------------------
  const repoFiles = [
    "ID.html",
    "index.html",
    "agent.html",
    "Axiom3E.link.js",
    "README.md"
  ];

  repoFiles.forEach(file => {
    system.files.push({
      file,
      exists: true,
      status: "OK"
    });
  });

  // ------------------------------------------------------
  // STATUS
  // ------------------------------------------------------
  system.status = system.errors.length === 0 ? "OK" : "WARN";

  return system;
}
